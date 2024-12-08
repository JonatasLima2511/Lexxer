def lex(expression: str, position: int):
    expr = expression
    lexem = ""

    i = position
    
    char = getNaoVazio(i, expr)
    charClass = getChar(char[1])

    if charClass == "LETRA":
        lexem += char[1]

        i = char[0]

        char = getNaoVazio(i + 1, expr)
        charClass = getChar(char[1])

        while charClass == "LETRA" or charClass == "DÍGITO":
            lexem += char[1]

            i = char[0]

            char = getNaoVazio(i + 1, expr)
            charClass = getChar(char[1])

        return [lexem, "IDENTIFICADOR", i]
    
    elif charClass == "DÍGITO":
        lexem += char[1]

        i = char[0]

        char = getNaoVazio(i + 1, expr)
        charClass = getChar(char[1])

        while charClass == "DÍGITO":

            lexem += char[1]

            i = char[0]

            char = getNaoVazio(i + 1, expr)
            charClass = getChar(char[1])

        return [lexem, "LITERALINTEIRO", i]
    
    elif charClass == "DESCONHECIDO":
        lexem = char[1]

        i = char[0]

        token = verificaToken(lexem)

        return [lexem, token, i]

    elif charClass == "FIMDEARQUIVO":
        return ["EOF", "FIMDEARQUIVO", i]




def getNaoVazio(index:int , expression: str):
    
    position = index
    expr = expression

    try:
        while expr[position] == " ":
            position += 1

        char = expr[position]

        return [position, char]
    except IndexError:
        return [len(expression), "EOF"]




def getChar(char: str):
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
