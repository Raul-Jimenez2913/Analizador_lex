from preprocess import tokenize_code

def build_suffix_array(seq):
    """
    Construye un arreglo de sufijos para la secuencia dada.
    Retorna una lista de tuplas (sufijo, posición).
    """
    suffixes = []
    for i in range(len(seq)):
        sufijo = seq[i:]        
        posicion = i
        suffixes.append((sufijo, posicion))
    suffixes.sort()
    return suffixes

def lcp(seq1, seq2):
    """Calcula el Longest Common Prefix entre dos secuencias."""
    count = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            count += 1
        else:
            break
    return count

def is_valid_match(start1, start2, length, covered1, covered2):
    """Verifica si un match no se superpone con matches anteriores."""
    for j in range(length):
        if start1 + j >= len(covered1) or start2 + j >= len(covered2):
            return False
        if covered1[start1 + j] or covered2[start2 + j]:
            return False
    return True

def mark_covered(start1, start2, length, covered1, covered2):
    """Marca tokens como cubiertos para evitar duplicados."""
    for j in range(length):
        if start1 + j < len(covered1):
            covered1[start1 + j] = True
        if start2 + j < len(covered2):
            covered2[start2 + j] = True

def find_common_chunks(seq1, seq2, min_lcp=4):
    """
    Encuentra los chunks comunes entre dos secuencias usando Suffix Arrays y LCP.
    Retorna el total de coincidencias, la longitud de la primera secuencia,
    la longitud de la segunda secuencia y una lista de coincidencias.
    """
    sep1, sep2 = ["#SEP1"], ["#SEP2"]
    combined = seq1 + sep1 + seq2 + sep2
    suffixes = build_suffix_array(combined)

    len_seq1 = len(seq1)
    offset_seq2 = len_seq1 + 1
    covered1 = [False] * len_seq1 if seq1 != seq2 else []
    covered2 = [False] * len(seq2) if seq1 != seq2 else []

    total_common = 0
    matches = []  # Se guardan coincidencias

    for i in range(1, len(suffixes)):
        suf1, idx1 = suffixes[i - 1]
        suf2, idx2 = suffixes[i]

        from_seq1_a = idx1 < len_seq1
        from_seq1_b = idx2 < len_seq1

        if from_seq1_a != from_seq1_b:
            length = lcp(suf1, suf2)

            if length >= min_lcp:
                if from_seq1_a:
                    start1 = idx1
                    start2 = idx2 - offset_seq2
                else:
                    start1 = idx2
                    start2 = idx1 - offset_seq2

                if start1 < 0 or start2 < 0:
                    continue

                if not covered1 or is_valid_match(start1, start2, length, covered1, covered2):
                    if covered1:
                        mark_covered(start1, start2, length, covered1, covered2)
                    total_common += length
                    matches.append(seq1[start1:start1 + length])  # ← Guarda el match

    return total_common, len_seq1, len(seq2), matches

def compute_similarity(seq1, seq2, min_lcp=4):
    """
    Calcula la similitud entre dos secuencias usando Suffix Arrays y LCP.
    Retorna un porcentaje entre 0.0 y 100.0.
    """
    if seq1 == seq2:
        return 100.0, [seq1]  # Toda la secuencia es común
    total_common, len1, len2, matches = find_common_chunks(seq1, seq2, min_lcp)
    total_len = len1 + len2
    sim = (2 * total_common / total_len) * 100 if total_len > 0 else 0.0
    return sim, matches

def compare_tokenized_suffix(path1, path2):
    """Compara dos archivos usando tokenización (via tokenize_code)."""
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    return compute_similarity(tokens1, tokens2)

def compare_plain_suffix(path1, path2):
    """Compara dos archivos como texto plano."""
    from io_utils import read_lines
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)
    seq1 = ' '.join(lines1).split()
    seq2 = ' '.join(lines2).split()
    return compute_similarity(seq1, seq2)