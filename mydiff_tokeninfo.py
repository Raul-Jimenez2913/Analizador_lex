import tokenize
from tokenize import TokenInfo
import difflib
from pathlib import Path
from io import BytesIO
import os

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
            print("=== Bloque Coincidente ===")
            print("Código 1:", " ".join(seq1[match.a:match.a+match.size]))
            print("Código 2:", " ".join(seq2[match.b:match.b+match.size]))
            print()
    if not found:
        print("No se encontraron bloques coincidentes largos.")

def analyze_pair(path1, path2):
    print(f"\nComparando: {os.path.basename(path1)} vs {os.path.basename(path2)}")
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    similarity = compute_similarity(tokens1, tokens2)
    print(f"\nSimilitud: {similarity:.2f}%")
    show_similar_sections(tokens1, tokens2)
    print("="*40 + "\n")

if __name__ == "__main__":
    # Análisis ejemplo DFS vs BFS
    analyze_pair("dfs.py", "bfs.py")
