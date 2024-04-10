from parser.classes import NumberLiteral, StringLiteral, VariableReference

def parse_arguments(tokens):
    pass


def parse_function_call(tokens):
    while True:
        param = next(tokens)
        print(param, "parse_function_call")

        comma = next(tokens)
        print(comma, "parse_function_call comma")

        if comma[0] not in ["COMMA", "RPAREN"]:
            raise Exception("Expected comma or )")

        if comma[0] == "RPAREN":
            return 


def parse_factor(tokens):
    token = next(tokens)
    print(token, "parse_factor")

    if token[0] == "NUMBER":
        return (NumberLiteral(token), None)
    
    if token[0] == "STRING":
        return (StringLiteral(token), None)

    if token[0] == "IDENT":
        variable = VariableReference(token)

        nextToken = next(tokens)
        print(nextToken, "nextToken")

        if nextToken[0] != "LPAREN":
            return (variable, nextToken)
        
    if token[0] == "LPAREN":
        return parse_expression(tokens)


def parse_term(tokens):
    terms = []
    
    terms.append(parse_factor(tokens))

    while True:
        nextToken = next(tokens)
        print(nextToken, "parse_term operation")

        if nextToken[0] not in ["TIMES", "DIVIDE"]:
            return (terms, nextToken)

        terms.append(nextToken)

        terms.append(parse_term(tokens))




def parse_expression(tokens):
    expressions = []

    [terms, nextToken] = parse_term(tokens)
    expressions.append(terms)

    if not nextToken: 
        nextToken = next(tokens)
    while True:
        print(nextToken, "parse_expression operation")

        if nextToken[0] not in ["PLUS", "MINUS"]:
            return (expressions, nextToken)

        expressions.append(nextToken)

        expressions.append(parse_term(tokens))
        nextToken = next(tokens)


def parse_variable_declaration(tokens):
    ident = next(tokens)

    if ident[0] != "IDENT":
        raise Exception("Expected identifier")
    
    assign = next(tokens)

    if assign[0] != "ASSIGN":
        raise Exception("Expected =")

    [expressions, semi] = parse_expression(tokens)

    print(semi, "semi")

    return expressions
        

def parse(tokens):
    ast = []

    for token in tokens:
        print(token, "parse")
        if token[0] == "KEYWORD":
            match(token[1]):
                case "vaw":
                    print(parse_variable_declaration(tokens))
