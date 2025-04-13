from diffutil_comparator import compare_plain as diff_plain, compare_tokenized as diff_tokens
from suffix_comparator import compare_plain as suffix_plain, compare_tokenized as suffix_tokens

files = [("dfs.py", "bfs.py")]

for path1, path2 in files:
    print(f"\nComparando {path1} vs {path2}")

    print("▶ Texto llano (DiffUtil):", f"{diff_plain(path1, path2):.2f}%")
    print("▶ Preprocesado (DiffUtil):", f"{diff_tokens(path1, path2):.2f}%")
    print("▶ Texto llano (Suffix Array):", f"{suffix_plain(path1, path2):.2f}%")
    print("▶ Preprocesado (Suffix Array):", f"{suffix_tokens(path1, path2):.2f}%")
    print("=" * 50)
