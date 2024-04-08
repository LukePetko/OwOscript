token_specification = [
    ('COMMENT',  r'//.*'),                # Comment
    ('NUMBER',   r'\d+(\.\d*)?'),         # Integer or decimal NUMBER
    ('IDENT',    r'[a-zA-Z_]\w*'),        # Identifiers
    ('STRING',   r'\".*?\"'),             # String
    ('EQ',       r'=='),                  # Equality
    ('ASSIGN',   r'='),                   # Assersion
    ('PLUS',     r'[\+]'),                # Plus
    ('MINUS',    r'[\-]'),                # Minus
    ('TIMES',    r'[\*]'),                # Times
    ('DIVIDE',   r'[/]'),                 # Divide
    ('LPAREN',   r'\('),                  # Left Parenthesis
    ('RPAREN',   r'\)'),                  # Right Parenthesis
    ('LBRACE',   r'\{'),                  # Left curly brace
    ('RBRACE',   r'\}'),                  # Right curly brace
    ('COMMA',    r','),                   # Comma
    ('NEWLINE',  r'\n'),                  # Line endings
    ('SEMI',     r';'),                   # Semicolon
    ('SKIP',     r'[ \t]+'),              # Skip over spaces and tabs
    ('MISMATCH', r'.')                    # Any other character
]

keyword_specification = [
    "vaw",
    "functiwoon",
    "wetuwn",
    "pwint"
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

