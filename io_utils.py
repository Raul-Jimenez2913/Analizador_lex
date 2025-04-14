import difflib
import os
from preprocess import tokenize_code
from suffix_comparator import compute_similarity

def read_lines(path):
    """
    Lee un archivo de texto línea por línea.
    Retorna una lista de líneas con saltos de línea incluidos.
    """
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def read_code(path):
    """
    Lee un archivo en modo binario.
    Útil si se desea comparar contenido exacto incluyendo codificación y bytes crudos.
    """
    with open(path, 'rb') as f:
        return f.read()
    
def show_diff_unix(path1, path2):
    """
    Muestra las diferencias entre dos archivos de texto
    utilizando el estilo de diff tipo UNIX (formato unificado).
    Muetras si los archivos son iguales.
    """
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)

    diff = difflib.unified_diff(
        lines1,
        lines2,
        fromfile=path1,
        tofile=path2,
        lineterm=''
    )

    output = list(diff)
    if not output:
        print("Archivos idénticos (texto plano).")
    else:
        print("Diferencias con UNIX diff:")
        for line in output:
            print(line)


def compute_similarity_from_plain(path1, path2):
    """
    Compara dos archivos como texto plano (no tokenizado).
    Lee el contenido de ambos archivos, separa el texto en palabras usando `split`,
    y calcula el porcentaje de similitud utilizando el comparador basado en Suffix Array.
    """
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)
    seq1 = ' '.join(lines1).split()
    seq2 = ' '.join(lines2).split()
    return compute_similarity(seq1, seq2)

def compute_similarity_from_tokens(path1, path2):
    """
    Compara dos archivos tokenizados léxicamente.
    Tokeniza ambos archivos usando `tokenize_code` y calcula la similitud
    usando el comparador basado en Suffix Array sobre los tokens normalizados.
    """
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    return compute_similarity(tokens1, tokens2)