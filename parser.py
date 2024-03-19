from classes import *

def parse_variable_declaration(tokens):
    name = next(tokens)

    if name[0] != 'IDENT':
        raise SyntaxError(f'Expected identifier, got {name[1]}')

    assign = next(tokens)

    if assign[0] != 'ASSIGN':
        raise SyntaxError(f'Expected =, got {assign[1]}')

    value = parse_expression(tokens)

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
                children.append(ReturnStatement(parse_expression(tokens)))
        elif token[0] == 'COMMENT':
            continue
        else:
            continue

def parse_expression(tokens, token = None):
    if token == None:
        token = next(tokens)
    try:
        nextToken = next(tokens)
    except StopIteration:
        match token[0]:
            case "NUMBER":
                return NumberLiteral(token)
            case "STRING":
                return StringLiteral(token)
            case "IDENT":
                return VariableReference(token)
        raise SyntaxError(f'Expected number, string or variable, got {token[1]}')
        
    match nextToken[0]:
        case "SEMI":
            # separate stuff like this
            match token[0]:
                case "NUMBER":
                    return NumberLiteral(token)
                case "STRING":
                    return StringLiteral(token)
                case "IDENT":
                    return VariableReference(token)
        case "OPERATOR":
            return parse_binary_expression(tokens, token, nextToken)
        case "LPAREN":
            return parse_function_execution(tokens, token)


def parse_binary_expression(tokens, left, operator):
    if left[0] not in ["NUMBER", "STRING", "IDENT"]:
        raise SyntaxError(f'Expected string, number or variable, got {left[1]}')

    match left[0]:
        case "NUMBER":
            left = NumberLiteral(left)
        case "STRING":
            left = StringLiteral(left)
        case "IDENT":
            left = VariableReference(left)

    if operator[0] in ["COMMENT", "SEMI"]:
        return left

    if operator[0] != "OPERATOR":
        raise SyntaxError(f'Expected operator, got {operator[1]}')

    right = next(tokens)

    if right[0] not in ["NUMBER", "STRING", "IDENT"]:
        raise SyntaxError(f'Expected operator, got {right[1]}')

    match right[0]:
        case "NUMBER":
            right = NumberLiteral(right)
        case "STRING":
            right = StringLiteral(right)
        case "IDENT":
            right = VariableReference(right)

    return BinaryOperation(left, right, operator)

def parse_function_execution(tokens, name):
    args = []

    while True:
        arg = next(tokens)

        if arg[0] == 'RPAREN':
            break
        elif arg[0] == 'COMMA':
            continue
        else:
            match arg[0]:
                case "NUMBER":
                    args.append(NumberLiteral(arg))
                case "STRING":
                    args.append(StringLiteral(arg))
                case "IDENT":
                    args.append(VariableReference(arg))


    return FunctionExecution(name, args)



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
        elif token[0] == "IDENT":
            ast.append(parse_expression(tokens, token))

    return ast

