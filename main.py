def lex(expression: str, position: int):
    expr = expression
    lexem = ""

    i = position
    
    char = getNaoVazio(i, expr)
    charClass = getChar(char[1])

    if charClass == "LETRA":
        lexem += char[1]

        i = char[0]

        char = getNaoVazio(i, expr)
        charClass = getChar(char[1])

        while charClass == "LETRA" or charClass == "DÍGITO":
            lexem += char[1]

            i = char[0]

            char = getNaoVazio(i, expr)
            charClass = getChar(char[1])

        return [lexem, "IDENTIFICADOR", i]
    
    elif charClass == "DÍGITO":
        lexem += char[1]

        i = char[0]

        char = getNaoVazio(i, expr)
        charClass = getChar(char[1])

        while charClass == "DÍGITO":

            lexem += char[1]

            i = char[0]

            char = getNaoVazio(i, expr)
            charClass = getChar(char[1])

        return [lexem, "LITERALINTEIRO", i]
    
    elif charClass == "DESCONHECIDO":
        lexem = char[1]

        token = verificaToken(lexem)

        return [lexem, token, i]

    elif charClass == "FIMDEARQUIVO":
        return ["EOF", "FIMDEARQUIVO", i]




def getNaoVazio(index:int , expression: str):
    
    if index > 0:
        position = index + 1
    else:
        position = index
    expr = expression

    try:
        while expr[position] == " ":
            position += 1

        char = expr[position]

        return [position, char]
    except IndexError:
        return [len(expression), "EOF"]




def getChar(character: str):
    char = character
    charClass = ""

    if char != "EOF":
        if char.isalpha():
            charClass = "LETRA"

        elif char.isnumeric():
            charClass = "DÍGITO"

        else:
            charClass = "DESCONHECIDO"

    else:
        charClass = "FIMDEARQUIVO"

    return charClass




def verificaToken(token):
    
    char = token
    tokenType = ""

    if char == "(":
        tokenType = "PARENTESESESQUERDO"
    elif char == ")":
        tokenType = "PARENTESESDIREITO"
    elif char == "+":
        tokenType = "OPSOMA"
    elif char == "-":
        tokenType = "OPSUBTRAÇÃO"
    elif char == "*":
        tokenType = "OPMULTIPLICAÇÃO"
    elif char == "/":
        tokenType = "OPDIVISÃO"

    return tokenType


# Exemplo de uso
expr = "(batata + pudim10)/3"

p = 0
lexema, token, position = lex(expr, p)

while token != "FIMDEARQUIVO":
    print (f"Lexema: {lexema}  Token: {token}")
    p = position + 1
    lexema, token, position = lex(expr, p)
