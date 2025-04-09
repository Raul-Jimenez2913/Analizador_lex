import tokenize
from tokenize import TokenInfo
import difflib
from pathlib import Path
from io import BytesIO
import os
import csv

def tokenize_code(filepath):
    with open(filepath, "rb") as f:
        tokens = tokenize.tokenize(f.readline)
        filtered = [t for t in tokens if t.type != tokenize.ENCODING]
        print(f"\nTokens en {os.path.basename(filepath)}:")
        for t in filtered:
            print(t)
        return filtered

def compute_similarity(tokens1, tokens2):
    seq1 = [t.string for t in tokens1]
    seq2 = [t.string for t in tokens2]
    matcher = difflib.SequenceMatcher(None, seq1, seq2)
    match_len = sum(m.size for m in matcher.get_matching_blocks())
    return match_len / min(len(seq1), len(seq2)) * 100

def show_similar_sections(tokens1, tokens2, min_size=5):
    seq1 = [t.string for t in tokens1]
    seq2 = [t.string for t in tokens2]
    matcher = difflib.SequenceMatcher(None, seq1, seq2)
    found = False
    for match in matcher.get_matching_blocks():
        if match.size >= min_size:
            found = True
            print("=== Bloque Coincidente ({} tokens)===".format(match.size))
            print("Código 1:", " ".join(seq1[match.a:match.a + match.size]))
            print("Código 2:", " ".join(seq2[match.b:match.b + match.size]))
            print()
    if not found:
        print("No se encontraron bloques coincidentes largos.")

def analyze_pair(path1, path2, results=None):
    print(f"\nComparando: {os.path.basename(path1)} vs {os.path.basename(path2)}")
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    similarity = compute_similarity(tokens1, tokens2)
    print(f"\nSimilitud: {similarity:.2f}%")
    show_similar_sections(tokens1, tokens2)
    print("="*40 + "\n")
    if results is not None:
        results.append((os.path.basename(path1), os.path.basename(path2), f"{similarity:.2f}"))

if __name__ == "__main__":
    results = []

    # Pares de prueba (puedes agregar más aquí)
    pairs = [
        ("dfs.py", "bfs.py")
        # Agrega más pares reales aquí si los tienes en tu carpeta
    ]

    for p1, p2 in pairs:
        analyze_pair(p1, p2, results)

    # Guardar resultados en CSV
    with open("similitud_python.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Archivo 1", "Archivo 2", "Similitud (%)"])
        writer.writerows(results)
