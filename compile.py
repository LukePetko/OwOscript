import re
from classes import VariableDeclaration, FunctionDeclaration

token_specification = [
    ('COMMENT',  r'//.*'),                # Comment
    ('NUMBER',   r'\d+(\.\d*)?'),         # Integer or decimal NUMBER
    ('IDENT',    r'[a-zA-Z_]\w*'),        # Identifiers
    ('STRING',   r'\".*?\"'),             # String
    ('EQ',       r'=='),                  # Equality
    ('ASSIGN',   r'='),                   # Assersion
    ('OPERATOR', r'[\+\-\*/]'),           # Math operations
    ('LPAREN',   r'\('),                  # Left Parenthesis
    ('RPAREN',   r'\)'),                  # Right Parenthesis
    ('LBRACE',   r'\{'),                  # Left curly brace
    ('RBRACE',   r'\}'),                  # Right curly brace
    ('COMMA',    r','),                   # Comma
    ('NEWLINE',  r'\n'),                  # Line endings
    ('SKIP',     r'[ \t;]+'),             # Skip over spaces and tabs
    ('MISMATCH', r'.')                    # Any other character
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

        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        else:
            if kind == 'IDENT' and value in keyword_specification:
                kind = 'KEYWORD'
            tokens.append((kind, value, line_num))

    return tokens


def parse_variable_declaration(tokens):
    name = next(tokens)

    if name[0] != 'IDENT':
        raise SyntaxError(f'Expected identifier, got {name[1]}')

    assign = next(tokens)

    if assign[0] != 'ASSIGN':
        raise SyntaxError(f'Expected =, got {assign[1]}')

    value = next(tokens) # TODO parse expressions

    return VariableDeclaration(name, value)

def parse_function_declaration(tokens):
    name = next(tokens)

    if name[0] != 'IDENT':
        raise SyntaxError(f'Expected identifier, got {name[1]}')

    left_paren = next(tokens)

    if left_paren[0] != 'LPAREN':
        raise SyntaxError(f'Expected (, got {left_paren[1]}')

    args = []

    while True:
        arg = next(tokens)

        if arg[0] == 'RPAREN':
            break
        elif arg[0] == 'COMMA':
            continue
        else:
            args.append(arg)

    left_brace = next(tokens)

    if left_brace[0] != 'LBRACE':
        raise SyntaxError(f'Expected {{, got {left_brace[1]}')

    body = parse_function_body(tokens)

    return FunctionDeclaration(name, args, body)
    
def parse_function_body(tokens):
    children = []
    while True:
        token = next(tokens)

        if token[0] == 'RBRACE':
            return children
        elif token[0] == 'KEYWORD':
            if token[1] == 'vaw':
                children.append(parse_variable_declaration(tokens))
        elif token[0] == 'COMMENT':
            continue
        else:
            print(token)





tokens = []

with open("template.owo", "r") as f:
    tokens = iter(lexer(f.read()))

# tokens = iter(lexer("vaw x = 5; // this is a comment\nvaw y = 10;"))

for token in tokens:
    if token[0] == "KEYWORD":
        match(token[1]):
            case "vaw":
                print(parse_variable_declaration(tokens))
            case "functiwoon":
                print(parse_function_declaration(tokens))
    elif token[0] == "COMMENT":
        continue

