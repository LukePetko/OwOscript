import re
from classes import BinaryOperation, NumberLiteral, ReturnStatement, StringLiteral, VariableDeclaration, FunctionDeclaration, VariableReference

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
    ('SEMI',     r';'),                   # Semicolon
    ('SKIP',     r'[ \t]+'),              # Skip over spaces and tabs
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

    value = parse_binary_expression(tokens)

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
            elif token[1] == 'wetuwn':
                children.append(ReturnStatement(parse_binary_expression(tokens)))
        elif token[0] == 'COMMENT':
            continue
        else:
            continue

def parse_binary_expression(tokens):
    left = next(tokens)

    if left[0] not in ["NUMBER", "STRING", "IDENT"]:
        raise SyntaxError(f'Expected string, number or variable, got {left[1]}')

    match left[0]:
        case "NUMBER":
            left = NumberLiteral(left)
        case "STRING":
            left = StringLiteral(left)
        case "IDENT":
            left = VariableReference(left)

    operation = None
    try:
        operation = next(tokens)
    except StopIteration:
        return left


    if operation[0] in ["COMMENT", "SEMI"]:
        return left

    if operation[0] != "OPERATOR":
        raise SyntaxError(f'Expected operation, got {operation[1]}')

    right = next(tokens)

    if right[0] not in ["NUMBER", "STRING", "IDENT"]:
        raise SyntaxError(f'Expected operation, got {right[1]}')

    match right[0]:
        case "NUMBER":
            right = NumberLiteral(right)
        case "STRING":
            right = StringLiteral(right)
        case "IDENT":
            right = VariableReference(right)

    return BinaryOperation(left, right, operation)

def parse(tokens):
    ast = []

    for token in tokens:
        if token[0] == "KEYWORD":
            match(token[1]):
                case "vaw":
                    ast.append(parse_variable_declaration(tokens))
                case "functiwoon":
                    ast.append(parse_function_declaration(tokens))
        elif token[0] == "COMMENT":
            continue

    return ast

ast = []

tokens = []

with open("testfile.owo", "r") as f:
    tokens = iter(lexer(f.read()))

# tokens = iter(lexer("vaw x = 5; // this is a comment\nvaw y = 10;"))
# tokens = iter(lexer("vaw x = 5"))

ast = parse(tokens)

print(ast)

