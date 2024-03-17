import re

token_specification = [
    ('COMMENT', r'//.*'),
    ('NUMBER',  r'\d+(\.\d*)?'),  # Integer or decimal NUMBER
    ('IDENT', r'[a-zA-Z_]\w*'),  # Identifiers
    ('STRING',  r'\".*?\"'),  # String
    ('ASSIGN', r'='), # Assersion
    ('OPERATOR', r'[\+\-\*/]'), # Math operations
    ('NEWLINE', r'\n'),  # Line endings
    ('SKIP',    r'[ \t;]+'),       # Skip over spaces and tabs
    ('MISMATCH', r'.')           # Any other character
]

keyword_specification = [
    "vaw",
    "functiwoon",
    "wetuwn",
    "pwint",
    "if",
    "ewse"
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

def lexer(code):
    tokens = []
    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        print(kind, value)

        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        # elif kind == 'MISMATCH':
        #     raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        else:
            if kind == 'IDENT' and value in keyword_specification:
                kind = 'KEYWORD'
            tokens.append((kind, value, line_num))





# with open("template.owo", "r") as f:
#     lexer(f.read())

lexer("vaw x = 5; // this is a comment\nvaw y = 10;")
