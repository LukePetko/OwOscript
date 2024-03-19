def semantic_analysis(ast):
    print(type(ast), type(ast.body))
    
    for node in ast.body:
        print(node.type)

