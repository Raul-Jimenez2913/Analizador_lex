import ply.lex as lex

# Lista de tokens
tokens = (
    'KEYWORD',
    'IDENTIFIER',
    'FLOAT',
    'INT_HEX',
    'INT_OCT',
    'INT_DEC',
    'STRING',
    'CHAR',
    'OPERATOR',
    'DELIMITER',
    'HEADER',
    'HASH',
)

# Palabras clave
keywords = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
    'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
    'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
    'volatile', 'while', 'include', 'define'
}

# Reglas simples con regex
t_HASH      = r'\#'
t_OPERATOR = r'==|!=|<=|>=|<<=|>>=|\+=|-=|\*=|/=|%=|&=|\|=|\^=|<<|>>|->|&&|\|\||\+\+|--|[-+*/%=<>&|^~!=.]'
t_DELIMITER = r'[{}\[\]();,]'
t_STRING    = r'"([^"\\]|\\.)*"'
t_CHAR      = r"'([^'\\]|\\.)'"

# Reglas para preprocesador (header)
def t_HEADER(t):
    r'<[a-zA-Z0-9_./]+\.h>|"[a-zA-Z0-9_./]+\.h"'
    return t

# Comentarios (ignorados)
def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass

# Espacios y tabs (ignorados)
t_ignore = ' \t'

# Reglara para números con decimales
def t_FLOAT(t):
    r'\d+\.\d*([eE][+-]?\d+)?|\d+[eE][+-]?\d+'
    t.value = float(t.value)
    return t

# Regla para números hexadecimales
def t_INT_HEX(t):
    r'0[xX][0-9a-fA-F]+'
    t.value = int(t.value, 16)
    return t

# Regla para números octales
def t_INT_OCT(t):
    r'0[0-7]+'
    t.value = int(t.value, 8)
    return t

# Regla para números decimales
def t_INT_DEC(t):
    r'(0|[1-9][0-9]*)'
    t.value = int(t.value)
    return t

# Regla para identificadores y palabras clave
def t_IDENTIFIER(t):
    r'\b[a-zA-Z_]\w*\b'
    if t.value in keywords:
        t.type = 'KEYWORD'
    return t

# Saltos de línea (actualiza el número de línea)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico: carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

if __name__ == "__main__":
    archivo = 'test.c'
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            code = f.read()
            lexer.input(code)
            for token in lexer:
                print(token)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {archivo}")