from diffutil_comparator import compare_plain as diff_plain, compare_tokenized as diff_tokens
from io_utils import show_diff_unix
from suffix_comparator import compare_plain_suffix as suffix_plain, compare_tokenized_suffix as suffix_tokens

files = [
    ("1648661.py", "1603390.py"),
    ("1603942.py", "1593943.py"),
    ("1552982.py", "1331742.py"),
    ("1552981.py", "1331721.py"),
    ("1648671.py", "1594065.py"),
    ("1611900.py", "1552856.py"),
    ("1594071.py", "1552861.py"),
    ("1552857.py", "1332025.py"),
    ("1653446.py", "1611948.py"),
    ("1648673.py", "1594744.py"),

]

for path1, path2 in files:
    print(f"\nComparando {path1} vs {path2}")

    print("* Texto llano (DiffUtil):", f"{diff_plain(path1, path2):.2f}%")
    print("* Preprocesado (DiffUtil):", f"{diff_tokens(path1, path2):.2f}%")
    print("* Texto llano (Suffix Array):", f"{suffix_plain(path1, path2):.2f}%")
    print("* Preprocesado (Suffix Array):", f"{suffix_tokens(path1, path2):.2f}%")
    show_diff_unix(path1, path2)
    print("-" * 50)