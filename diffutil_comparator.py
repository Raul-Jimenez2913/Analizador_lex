import difflib
from io_utils import read_lines
from preprocess import tokenize_code

def compare_plain(path1, path2):
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)
    seq1 = ' '.join(lines1).split()
    seq2 = ' '.join(lines2).split()
    matcher = difflib.SequenceMatcher(None, seq1, seq2)
    return matcher.ratio() * 100

def compare_tokenized(path1, path2):
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    matcher = difflib.SequenceMatcher(None, tokens1, tokens2)
    ratio = matcher.ratio() * 100
    return ratio
