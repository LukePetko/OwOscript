from classes import *

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

