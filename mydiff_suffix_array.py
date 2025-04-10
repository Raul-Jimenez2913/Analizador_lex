import tokenize
import os
import csv

# Prueba de uso de diff (Unix)
# import difflib

# def compare_with_diffutil(path1, path2):
#     with open(path1, 'r', encoding='utf-8') as f1, open(path2, 'r', encoding='utf-8') as f2:
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()

#     print(f"\nDiferencias tipo UNIX diff: {os.path.basename(path1)} vs {os.path.basename(path2)}\n")

#     diff = list(difflib.unified_diff(
#         lines1,
#         lines2,
#         fromfile=path1,
#         tofile=path2,
#         lineterm=''
#     ))

#     if not diff:
#         print("Archivos idénticos (en texto).")
#     else:
#         for line in diff:
#             print(line)

# Tokenización del código fuente con filtrado
def tokenize_code(filepath):
    with open(filepath, "rb") as f:
        tokens = tokenize.tokenize(f.readline)
        return [
            t.string for t in tokens
            if t.type not in (
                tokenize.ENCODING,
                tokenize.NEWLINE,
                tokenize.NL,
                tokenize.INDENT,
                tokenize.DEDENT,
                tokenize.ENDMARKER,
                tokenize.COMMENT
            )
        ]

# Construcción de sufijos (listas de tokens)
def build_suffix_array(tokens):
    return sorted((tokens[i:], i) for i in range(len(tokens)))

# Longest common prefix entre dos listas de tokens
def lcp(seq1, seq2):
    count = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            count += 1
        else:
            break
    return count

# Comparación entre dos secuencias de tokens con suffix array
def compute_similarity_suffix(seq1, seq2):
    sep1 = ["#END1"]
    sep2 = ["#END2"]
    combined = seq1 + sep1 + seq2 + sep2
    suffixes = build_suffix_array(combined)

    total_common = 0
    common_chunks = []

    len_seq1 = len(seq1)
    for i in range(1, len(suffixes)):
        s1, idx1 = suffixes[i - 1]
        s2, idx2 = suffixes[i]

        # Solo comparar si son de diferentes archivos
        from_seq1 = idx1 < len(seq1)
        from_seq2 = idx2 < len(seq1)
        if from_seq1 != from_seq2:
            length = lcp(s1, s2)
            if length >= 5:  # Ajustar el umbral
                total_common += length
                common_chunks.append(s1[:length])

    avg_length = (len(seq1) + len(seq2)) / 2
    similarity = (total_common / avg_length) * 100 if avg_length > 0 else 0.0
    return similarity, common_chunks

# Mostrar secciones comunes
def print_common_chunks(chunks):
    print("\nSecciones similares detectadas:")
    for i, chunk in enumerate(chunks, 1):
        print(f"\n--- Subcadena común #{i} ({len(chunk)} tokens) ---")
        print(" ".join(chunk))

# Analiza un par de archivos
def analyze_pair(path1, path2, results=None):
    print(f"\nComparando: {os.path.basename(path1)} vs {os.path.basename(path2)}")
    seq1 = tokenize_code(path1)
    seq2 = tokenize_code(path2)

    similarity, chunks = compute_similarity_suffix(seq1, seq2)
    print(f"\nSimilitud estimada: {similarity:.2f}%")
    print("=" * 40)
    print_common_chunks(chunks)

    if results is not None:
        results.append((os.path.basename(path1), os.path.basename(path2), f"{similarity:.2f}"))

# Main
if __name__ == "__main__":
    results = []

    # Cambia estos por tus propios archivos
    pairs = [
        ("dfs.py", "bfs.py")
    ]

    for p1, p2 in pairs:
        analyze_pair(p1, p2, results)
        #compare_with_diffutil(p1, p2)

    # Guarda resultados CSV
    with open("similitud_tokens_suffix_array.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Archivo 1", "Archivo 2", "Similitud (%)"])
        writer.writerows(results)