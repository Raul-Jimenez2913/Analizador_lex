import tokenize
from tokenize import TokenInfo
from pathlib import Path
import os
import csv

def tokenize_code(filepath):
    with open(filepath, "rb") as f:
        tokens = tokenize.tokenize(f.readline)
        filtered = [t for t in tokens if t.type != tokenize.ENCODING]
        print(f"\nTokens en {os.path.basename(filepath)}:")
        for t in filtered:
            print(t)
        return [t.string for t in filtered]

def build_suffix_array(seq):
    return sorted((seq[i:], i) for i in range(len(seq)))

def lcp(s1, s2):
    count = 0
    for a, b in zip(s1, s2):
        if a == b:
            count += 1
        else:
            break
    return count

def compute_similarity_suffix(seq1, seq2):
    # Concatenar ambos con separador único
    combined = seq1 + ["#"] + seq2 + ["$"]
    suffixes = build_suffix_array(combined)
    
    total_common = 0
    for i in range(1, len(suffixes)):
        sa1, idx1 = suffixes[i - 1]
        sa2, idx2 = suffixes[i]
        # Asegurarse de que provienen de distintas secuencias
        if (idx1 < len(seq1)) != (idx2 < len(seq1)):
            total_common += lcp(sa1, sa2)

    return total_common / min(len(seq1), len(seq2)) * 100

def analyze_pair_suffix(path1, path2, results=None):
    print(f"\nComparando (Suffix Array): {os.path.basename(path1)} vs {os.path.basename(path2)}")
    seq1 = tokenize_code(path1)
    seq2 = tokenize_code(path2)
    similarity = compute_similarity_suffix(seq1, seq2)
    print(f"\nSimilitud estimada: {similarity:.2f}%")
    print("="*40 + "\n")
    if results is not None:
        results.append((os.path.basename(path1), os.path.basename(path2), f"{similarity:.2f}"))

if __name__ == "__main__":
    results = []

    # Pares de archivos para comparar
    pairs = [
        ("dfs.py", "bfs.py")
        # Puedes añadir más aquí
    ]

    for p1, p2 in pairs:
        analyze_pair_suffix(p1, p2, results)

    # Guardar resultados
    with open("similitud_suffix_array.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Archivo 1", "Archivo 2", "Similitud (%)"])
        writer.writerows(results)
