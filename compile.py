from parser.classes import AST
from lexer import lexer
from parser.parser_new import parse
from semantic_analysis import semantic_analysis

ast = []

tokens = []

file = ""

with open("testfile.owo", "r") as f:
    file = f.read()
    tokens = lexer(file)

# print(tokens)

# tokens = iter(lexer("vaw x = 5; // this is a comment\nvaw y = 10;"))
# tokens = iter(lexer("vaw x = 5"))

print(file)

ast = AST(parse(iter(tokens)))
#
# semantic_analysis(ast)
#
