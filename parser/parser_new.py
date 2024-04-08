from parser.classes import NumberLiteral, StringLiteral, VariableReference


def parse_factor(tokens):
    token = next(tokens)

    if token[0] == "NUMBER":
        return NumberLiteral(token)
    
    if token[0] == "STRING":
        return StringLiteral(token)

    if token[0] == "IDENT":
        return VariableReference(token)

    if token[0] == "LPAREN":
        return parse_expression(tokens)

def parse_term(tokens):
    

def parse_expression(tokens):
    
    

    return next(tokens)

def parse_print(tokens):
    ident = next(tokens)

    if ident[0] != "IDENT":
        raise Exception("Expected identifier")
    
    assign = next(tokens)

    if assign[0] != "ASSIGN":
        raise Exception("Expected =")

    semi = parse_expression(tokens)

    print(semi)


        

def parse(tokens):
    ast = []

    for token in tokens:
        if token[0] == "KEYWORD":
            match(token[1]):
                case "vaw":
                    parse_print(tokens)
