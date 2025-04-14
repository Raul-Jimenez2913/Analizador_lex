import os
import csv
from diffutil_comparator import compare_plain as diff_plain, compare_tokenized as diff_tokens
from suffix_comparator import compare_plain_suffix as suffix_plain, compare_tokenized_suffix as suffix_tokens
from io_utils import compute_similarity_from_plain, compute_similarity_from_tokens, show_diff_unix

def main():
    # Variable para usar o no Diff de Unix
    use_diff = False

    # Lista de archivos a comparar
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

    # Crear archivo CSV para resultados
    with open("resultados_suffix.csv", "w", newline='', encoding="utf-8") as suffix_file, \
         open("resultados_diffutil.csv", "w", newline='', encoding="utf-8") as diff_file:

        suffix_writer = csv.writer(suffix_file)
        diff_writer = csv.writer(diff_file)

        suffix_writer.writerow([
            "Archivo 1", "Archivo 2",
            "Texto llano (Suffix Array)", "Tokenizado (Suffix Array)",
            "Coincidencias SA (TP)", "Coincidencias SA (TK)"
        ])
        diff_writer.writerow([
            "Archivo 1", "Archivo 2",
            "Texto llano (DiffUtil)", "Tokenizado (DiffUtil)",
            "Coincidencias Diff (TP)", "Coincidencias Diff (TK)"
        ])

        for path1, path2 in files:
            print(f"\nComparando {path1} vs {path2}")
            path1 = os.path.join("dataset/", path1)
            path2 = os.path.join("dataset/", path2)
            
            # Comparaciones
            sim_plain, plain_matches = compute_similarity_from_plain(path1, path2)
            sim_tok, tok_matches = compute_similarity_from_tokens(path1, path2)
            sim_diff_plain, diff_plain_matches = diff_plain(path1, path2)
            sim_diff_tok, diff_tok_matches = diff_tokens(path1, path2)

            # Mostrar en terminal
            print(f"* Texto llano (DiffUtil): {sim_diff_plain:.2f}%")
            print(f"* Preprocesado (DiffUtil): {sim_diff_tok:.2f}%")
            print(f"* Texto llano (Suffix Array): {sim_plain:.2f}%")
            print(f"* Preprocesado (Suffix Array): {sim_tok:.2f}%")
            
            if use_diff:
                show_diff_unix(path1, path2)

            print("-" * 50)

            # Suffix Array CSV
            suffix_writer.writerow([
                path1, path2,
                f"{sim_plain:.2f}%", f"{sim_tok:.2f}%",
                ' | '.join(' '.join(match) for match in plain_matches),
                ' | '.join(' '.join(match) for match in tok_matches)
            ])

            # DiffUtil CSV
            diff_writer.writerow([
                path1, path2,
                f"{sim_diff_plain:.2f}%", f"{sim_diff_tok:.2f}%",
                ' | '.join(' '.join(match) for match in diff_plain_matches),
                ' | '.join(' '.join(match) for match in diff_tok_matches)
            ])


if __name__ == "__main__":
    main()