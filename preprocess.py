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


## tokenizador complejo
# import tokenize
# import keyword
# import token

# def tokenize_code(path):
#     with open(path, "rb") as f:
#         tokens = tokenize.tokenize(f.readline)

#         name_map = {}
#         counter = 1
#         output = []

#         for t in tokens:
#             # Saltar tokens irrelevantes
#             if t.type in (
#                 tokenize.ENCODING,
#                 tokenize.NEWLINE,
#                 tokenize.NL,
#                 tokenize.INDENT,
#                 tokenize.DEDENT,
#                 tokenize.ENDMARKER,
#                 tokenize.COMMENT
#             ):
#                 continue

#             # Anonimizar identificadores (variables, funciones, clases)
#             if t.type == tokenize.NAME and not keyword.iskeyword(t.string):
#                 if t.string not in name_map:
#                     name_map[t.string] = f"ID_{counter}"
#                     counter += 1
#                 output.append(name_map[t.string])

#             # Normalizar literales (números, strings, True/False, None)
#             elif t.type in (tokenize.NUMBER, tokenize.STRING):
#                 output.append("CONST")

#             elif t.string in {"True", "False", "None"}:
#                 output.append("CONST")

#             else:
#                 output.append(t.string)

#         return output
