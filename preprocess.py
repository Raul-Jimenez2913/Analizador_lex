import tokenize

def tokenize_code(path):
    with open(path, "rb") as f:
        tokens = tokenize.tokenize(f.readline)
        return [
            t.string for t in tokens
            if t.type not in (
                tokenize.ENCODING,
                tokenize.NEWLINE,
                tokenize.NL,
                tokenize.INDENT,
                tokenize.DEDENT,
                tokenize.ENDMARKER,
                tokenize.COMMENT
            )
        ]
