from diffutil_comparator import compare_plain as diff_plain, compare_tokenized as diff_tokens
from io_utils import show_diff_unix
from suffix_comparator import compare_plain_suffix as suffix_plain, compare_tokenized_suffix as suffix_tokens

files = [
    ("1012762.py", "1374351.py"),
    ("1012763.py", "1379734.py"),
    ("1012765.py", "1382951.py"),
    ("1021397.py", "1383293.py"),
    ("1120019.py", "1383493.py"),
    ("1160494.py", "1386802.py"),
    ("1251345.py", "1386864.py"),
    ("1271278.py", "1434903.py"),
    ("1331742.py", "1562575.py"),
    ("1369343.py", "1574383.py"),
]

for path1, path2 in files:
    print(f"\nComparando {path1} vs {path2}")

    print("* Texto llano (DiffUtil):", f"{diff_plain(path1, path2):.2f}%")
    print("* Preprocesado (DiffUtil):", f"{diff_tokens(path1, path2):.2f}%")
    print("* Texto llano (Suffix Array):", f"{suffix_plain(path1, path2):.2f}%")
    print("* Preprocesado (Suffix Array):", f"{suffix_tokens(path1, path2):.2f}%")
    show_diff_unix(path1, path2)
    print("-" * 50)