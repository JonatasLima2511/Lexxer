from lexxer import lex

def parser(expression):

    def proximo_token():
        nonlocal token, lexem, position

        if token != "FIMDEARQUIVO":
            lexem, token, position = lex(expression, position + 1)



    def expr():
        term()

        while token in ("OPSOMA", "OPSUBTRAÇÃO"):
            proximo_token()
            
            term()



    def term():
        factor()

        while token in ("OPMULTIPLICAÇÃO", "OPDIVISÃO"):
            proximo_token()

            factor()



    def factor():

        if token in ("IDENTIFICADOR", "LITERALINTEIRO"):
            proximo_token()

        elif token == "PARENTESESESQUERDO":
            proximo_token()

            expr()

            if token == "PARENTESESDIREITO":
                proximo_token()

            else:
                raise SyntaxError("Esperado PARENTESESDIREITO, mas encontrado outro token.")
            
        else:
            raise SyntaxError(f"Token inesperado: {token}")

    # Inicializando do analisador
    position = 0
    lexem, token, position = lex(expression, position)

    try:
        expr()

        if token != "FIMDEARQUIVO":
            raise SyntaxError("Tokens restantes após o fim da análise.")
        
        print("Expressão válida!")

    except SyntaxError as e: 
        print(f"Erro de sintaxe: {e}")
