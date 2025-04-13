import difflib

def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def read_code(path):
    with open(path, 'rb') as f:
        return f.read()
    
def show_diff_unix(path1, path2):
    lines1 = read_lines(path1)
    lines2 = read_lines(path2)

    diff = difflib.unified_diff(
        lines1,
        lines2,
        fromfile=path1,
        tofile=path2,
        lineterm=''  # no agrega \n extra
    )

    output = list(diff)
    if not output:
        print("Archivos idénticos (texto plano).")
    else:
        print("Diferencias estilo UNIX diff:")
        for line in output:
            print(line)
