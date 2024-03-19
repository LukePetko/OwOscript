from classes import AST
from lexer import lexer
from parser import parse
from semantic_analysis import semantic_analysis

ast = []

tokens = []

with open("testfile.owo", "r") as f:
    tokens = iter(lexer(f.read()))

# tokens = iter(lexer("vaw x = 5; // this is a comment\nvaw y = 10;"))
# tokens = iter(lexer("vaw x = 5"))

ast = AST(parse(tokens))

semantic_analysis(ast)

