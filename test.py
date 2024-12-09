# Exemplo de uso

from lexxer import lex
from parser import parser

expression = "(batata + pudim10)/3"

p = 0
lexema, token, position = lex(expression, p)

print("Analise léxica: \n")

while token != "FIMDEARQUIVO":
    print (f"Lexema: {lexema}  Token: {token}")

    p = position + 1
    lexema, token, position = lex(expression, p)

print("\nAnálise Sintática:")

parser(expression)
