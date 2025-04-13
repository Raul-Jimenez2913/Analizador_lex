def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def read_code(path):
    with open(path, 'rb') as f:
        return f.read()