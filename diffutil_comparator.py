import difflib
from io_utils import read_lines
from preprocess import tokenize_code

def compare_plain(path1, path2):
    """
    Compara dos archivos como texto plano.
    Tokeniza por palabras (usando split) y calcula similitud con difflib.
    """
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)
    seq1 = ' '.join(lines1).split()
    seq2 = ' '.join(lines2).split()
    matcher = difflib.SequenceMatcher(None, seq1, seq2)
    similaridad = round(matcher.ratio() * 100, 2)

    coincidencias = []
    for match in matcher.get_matching_blocks():
        a, b, length = match
        if length >= 4:
            coincidencias.append(seq1[a:a+length])

    return similaridad, coincidencias

def compare_tokenized(path1, path2):
    """
    Compara dos archivos usando tokenización léxica (via tokenize_code).
    Calcula similitud con difflib.
    """
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    matcher = difflib.SequenceMatcher(None, tokens1, tokens2)
    similaridad = round(matcher.ratio() * 100, 2)

    coincidencias = []
    for match in matcher.get_matching_blocks():
        a, b, length = match
        if length >= 4:
            coincidencias.append(tokens1[a:a+length])

    return similaridad, coincidencias
