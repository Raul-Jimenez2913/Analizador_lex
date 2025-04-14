from diffutil_comparator import compare_plain as diff_plain, compare_tokenized as diff_tokens
from io_utils import show_diff_unix
from suffix_comparator import compare_plain_suffix as suffix_plain, compare_tokenized_suffix as suffix_tokens

files = [
    ("1531746.py", "1679741.py"),
    ("1012763.py", "1012765.py"),
    ("1308327.py", "1308139.py"),
    ("1021922.py", "1021919.py"),
    ("1478030.py", "1478027.py"),
    ("1357280.py", "1357277.py"),
    ("1534024.py", "1474762.py"),
    ("1604158.py", "1601396.py"),
    ("1272054.py", "1155981.py"),
    ("1160494.py", "1479692.py"),
]

for path1, path2 in files:
    print(f"\nComparando {path1} vs {path2}")

    print("* Texto llano (DiffUtil):", f"{diff_plain(path1, path2):.2f}%")
    print("* Preprocesado (DiffUtil):", f"{diff_tokens(path1, path2):.2f}%")
    print("* Texto llano (Suffix Array):", f"{suffix_plain(path1, path2):.2f}%")
    print("* Preprocesado (Suffix Array):", f"{suffix_tokens(path1, path2):.2f}%")
    show_diff_unix(path1, path2)
    print("-" * 50)