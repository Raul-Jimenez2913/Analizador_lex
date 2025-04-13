from preprocess import tokenize_code

def build_suffix_array(seq):
    suffixes = []
    for i in range(len(seq)):
        sufijo = seq[i:]        
        posicion = i
        suffixes.append((sufijo, posicion))
    suffixes.sort()
    return suffixes

def lcp(seq1, seq2):
    count = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            count += 1
        else:
            break
    return count

def compute_similarity(seq1, seq2, min_lcp=4):
    sep1 = ["#SEP1"]
    sep2 = ["#SEP2"]
    combined = seq1 + sep1 + seq2 + sep2

    suffixes = build_suffix_array(combined)

    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    offset_seq2 = len(seq1) + 1  # posición en combined donde inicia seq2

    covered1 = [False] * len_seq1
    covered2 = [False] * len_seq2

    total_common = 0

    for i in range(1, len(suffixes)):
        suf1, idx1 = suffixes[i - 1]
        suf2, idx2 = suffixes[i]

        # Determinar de qué secuencia viene cada sufijo
        from_seq1_a = idx1 < len_seq1
        from_seq1_b = idx2 < len_seq1

        # Comparar solo si vienen de archivos distintos
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

                overlap = False
                for j in range(length):
                    if start1 + j >= len(covered1) or start2 + j >= len(covered2):
                        overlap = True
                        break
                    if covered1[start1 + j] or covered2[start2 + j]:
                        overlap = True
                        break

                if not overlap:
                    for j in range(length):
                        if start1 + j < len(covered1):
                            covered1[start1 + j] = True
                        if start2 + j < len(covered2):
                            covered2[start2 + j] = True
                    total_common += length

    min_len = min(len_seq1, len_seq2)
    return (2 * total_common / (len_seq1 + len_seq2)) * 100 if (len_seq1 + len_seq2) > 0 else 0.0

def compare_tokenized_suffix(path1, path2):
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    return compute_similarity(tokens1, tokens2)

def compare_plain_suffix(path1, path2):
    from io_utils import read_lines
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)
    seq1 = ' '.join(lines1).split()
    seq2 = ' '.join(lines2).split()

    return compute_similarity(seq1, seq2)
