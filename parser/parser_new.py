def parse_factor(tokens):
    token = next(tokens)

    if token[0] == "NUMBER":
        return ("NUMBER", token[1])
    elif token[0] == "LPAREN":
        expr = parse_expr(tokens)
        token = next(tokens)
        assert token[0] == "RPAREN"
        return expr
    elif token[0] == "STRING":
        return ("STRING", token[1])
    elif token[0] == "IDENT":
        return ("IDENT", token[1])

def parse_term(tokens):
    left = parse_factor(tokens)
    token = next(tokens)
    

def parse(tokens):
    ast = []

    for token in tokens:
        if token[0] == "KEYWORD":
            match(token[1]):
                case "pwint":
                    pass
