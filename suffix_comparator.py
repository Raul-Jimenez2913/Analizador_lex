from preprocess import tokenize_code

def build_suffix_array(seq):
    return sorted((seq[i:], i) for i in range(len(seq)))

def lcp(seq1, seq2):
    count = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            count += 1
        else:
            break
    return count

def compute_similarity(seq1, seq2):
    sep1 = ["#END1"]
    sep2 = ["#END2"]
    combined = seq1 + sep1 + seq2 + sep2
    suffixes = build_suffix_array(combined)

    total_common = 0
    len_seq1 = len(seq1)
    for i in range(1, len(suffixes)):
        s1, idx1 = suffixes[i - 1]
        s2, idx2 = suffixes[i]
        if (idx1 < len_seq1) != (idx2 < len_seq1):
            length = lcp(s1, s2)
            if length >= 5:
                total_common += length

    avg_len = (len(seq1) + len(seq2)) / 2
    return (total_common / avg_len) * 100 if avg_len else 0

def compare_tokenized(path1, path2):
    tokens1 = tokenize_code(path1)
    tokens2 = tokenize_code(path2)
    return compute_similarity(tokens1, tokens2)

def compare_plain(path1, path2):
    from io_utils import read_lines
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)
    return compute_similarity(lines1, lines2)
