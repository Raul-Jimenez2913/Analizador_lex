import re

# Definiciones de tokens (subconjunto de C
KEYWORDS = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
    'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
    'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
    'volatile', 'while'
}

TOKEN_REGEX = [
    ('COMMENT', r'//.*|/\*[\s\S]*?\*/'),
    ('STRING', r'"([^"\\]|\\.)*"'),
    ('CHAR', r"'([^'\\]|\\.)'"),
    ('NUMBER', r'\b\d+(\.\d+)?([eE][+-]?\d+)?\b'),
    ('KEYWORD', r'\b(?:' + '|'.join(KEYWORDS) + r')\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
    ('OPERATOR', r'==|!=|<=|>=|\+\+|--|&&|\|\||[-+*/%=<>!&|^~]'),
    ('DELIMITER', r'[{}()\[\];,]'),
    ('WHITESPACE', r'\s+'),
    ('UNKNOWN', r'.'),
]

def tokenize(code):
    tokens = []
    while code:
        for token_type, regex in TOKEN_REGEX:
            match = re.match(regex, code)
            if match:
                value = match.group(0)
                if token_type not in {'WHITESPACE', 'COMMENT'}:
                    tokens.append((token_type, value))
                code = code[len(value):]
                break
    return tokens

# Prueba
if __name__ == "__main__":
    test_code = '''
    int main() {
        // Este es un comentario
        int x = 42;
        if (x > 0) {
            printf("Hola mundo!\\n");
        }
        return 0;
    }
    '''

    result = tokenize(test_code)
    for tok in result:
        print(tok)