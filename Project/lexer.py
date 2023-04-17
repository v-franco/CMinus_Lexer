# Programa Lexer 
# Realizado por:
# Juan Pablo Ortiz Ortega A01366969 
# Victor Hugo Franco Juárez A01366475


from globalTypes import *


lineno = 1 # almacena el no. de lineas
isError = True # Bandera de error para validar la posición del error


# función globales() recibe del main.py el programa, la posición del lexer, y la longitud
def globales(prog, pos, long):
    global program
    global position
    global programLength
    program = prog
    position = pos
    programLength = long


# función reservedLookup() recibe el string de un token ID para validar si no es una palabra reservada
def reservedLookup(tokenString):
    for w in ReservedWords:
        if tokenString == w.value:
            return TokenType(tokenString)
    return TokenType.ID


# fucnión printError imprime el mensaje de error y la posición con el acent circunflejo indicando el error
# Recibe la línea, la posición del error, y sí el error es en la formación de un token NOT_EQUAL_TO
def printError(line, errorPosi, errorType):
    global isError 
    currLine = 0
    line -= 1
    lineString = ""
    errorMarkCounter = 0
    currPos = 0 #Final de la línea
    errorLineLen = 0
    errorSpaces = ""
    # Se encuentra la línea en donde se encuentra el error y consigue la longitud de la línea, así como 
    # la posición del final de esta
    for i in (program):
        if (i == "\n"):
            currLine += 1
        if (currLine == line):
            lineString += i
            errorMarkCounter +=1
            errorLineLen += 1
        if (currLine > line):
            break
        currPos += 1
    # Cálculo de la posición del acento circunflejo según la longitud de la línea y dónde
    # se encontró el error
    circumPos = errorLineLen - (currPos - errorPosi)
    errorSpaces = " " * circumPos
    print(lineString)
    if(errorType == 1):
        print(errorSpaces[:-1], "^","\n")
    else:
        print(errorSpaces[:-2], "^","\n")
    isError = True

    

                
# Funcion getToken identifica e imprime los tokens del programa en C-
# Utiliza matriz de estados obtenida de un automata
def getToken(imprime = True):
    global position, lineno, isError
    
    errorPos = 0 # posicion de error
    errorType = 0 # bool para identificar si el error es en un IS_NOT_EQUAL o no


    #Matriz de estados generada de un automata
    M = [[1,3,0,24,22,20,42,12,16,9,5,26,28,30,32,34,36,38,40,1000],
    [1,47,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [48,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [6,6,6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [999,999,999,999,999,999,999,999,999,999,10,999,999,999,999,999,999,999,999,999],
    [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [13,13,13,13,13,13,13,13,13,13,14,13,13,13,13,13,13,13,13,13],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [17,17,17,17,17,17,17,17,17,17,18,17,17,17,17,17,17,17,17,17],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [43,43,43,43,43,44,43,43,43,43,43,43,43,43,43,43,43,43,43,43],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [44,44,44,44,44,45,44,44,44,44,44,44,44,44,44,44,44,44,44,999],
    [44,44,44,44,44,44,46,44,44,44,44,44,44,44,44,44,44,44,44,999],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [47,47,999,999,999,999,999,999,999,999,10,999,999,999,999,999,999,999,999,999],
    [48,48,999,999,999,999,999,999,999,999,10,999,999,999,999,999,999,999,999,999],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000]]

    estado = 0 # estado de acuerdo con la matriz
    lex = '' # lexema 
    token = '' #token identificado

    while (token == ""):
        c = program[position] #carácter actual

        # Condición especial para comentarios no cerrados
        if (estado == 44 or estado == 45):
            auxLex = lex 
            auxLex += c
            if ("$" in auxLex):
                print("Line:",lineno, "ERROR comentario no cerrado")

        # Determina columna de la matriz dependiendo del carácter
        if c.isdigit():
            col = 0
        elif c.isalpha():
            col = 1
        elif ((c == ' ') or (c == '\t') or (c == '\n')):
            col = 2
            # Detecta un salto de línea y se suma "uno" al contador de líneas
            if (c == "\n"):
                lineno += 1 
        elif c == "+":
            col = 3
        elif c == "-":
            col = 4
        elif c == '*':
            col = 5
        elif c == '/':
            col = 6
        elif c == "<":
            col = 7
        elif c == ">":
            col = 8
        elif c == "!":
            col = 9
        elif c == "=":
            col = 10
        elif c == ";":
            col = 11
        elif c == ",":
            col = 12
        elif c == "(":
            col = 13
        elif c == ")":
            col = 14
        elif c == "[":
            col = 15
        elif c == "]":
            col = 16
        elif c == "{":
            col = 17
        elif c == "}":
            col = 18
        elif c == "$":
            col = 19

        # Cambio de estado según la matriz
        estado = M[estado][col]

        # Validación de estados finales (Detección de tokens o error)
        if estado == 2:
            token = TokenType.INT
            lex += c
            estado = 0
            position -= 1
        elif estado == 4:
            token = TokenType.ID
            lex += c
            estado = 0 
            position -= 1
            token = reservedLookup(lex[:-1]) #Valida sí el ID es una palabra reservada
        elif estado == 6:
            token = TokenType.ASSIGN
            lex += c
            estado = 0
            position -= 1
        elif estado == 8:
            token = TokenType.EQUAL_TO
            lex += c
            estado = 0
            position -= 1
        elif estado == 11:
            token = TokenType.NOT_EQUAL_TO
            lex += c
            estado = 0
        elif estado == 13:
            token = TokenType.LESS_THAN
            lex += c
            estado = 0
        elif estado == 15:
            token = TokenType.LESS_OR_EQUAL_TO
            lex += c
            estado = 0
        elif estado == 17:
            token = TokenType.MORE_THAN
            lex += c
            estado = 0
        elif estado == 18:
            token = TokenType.MORE_OR_EQUAL_TO
            lex += c
            estado = 0
            lex += "="
        elif estado == 21:
            token = TokenType.TIMES
            lex += c
            estado = 0
            position -= 1
        elif estado == 23:
            token = TokenType.MINUS
            lex += c
            estado = 0
            position -= 1
        elif estado == 25:
            token = TokenType.PLUS
            lex += c
            estado = 0
            position -= 1
        elif estado == 27:
            token = TokenType.SEMI
            lex += c
            estado = 0
            position -= 1
        elif estado == 29:
            token = TokenType.COMMA
            lex += c
            estado = 0
            position -= 1
        elif estado == 31:
            token = TokenType.LPAREN
            lex += c
            estado = 0
            position -= 1

        elif estado == 33:
            token = TokenType.RPAREN
            lex += c
            estado = 0
            position -= 1
        elif estado == 35:
            token = TokenType.LBRACKET
            lex += c
            estado = 0
            position -= 1
        elif estado == 37:
            token = TokenType.RBRACKET
            lex += c
            estado = 0
            position -= 1
        elif estado == 39:
            token = TokenType.LCURLY
            lex += c
            estado = 0
            position -= 1
        elif estado == 41:
            token = TokenType.RCURLY
            lex += c
            estado = 0
            position -= 1
        elif estado == 43:
            token = TokenType.SLASH
            lex += c
            estado = 0
            position -= 1
        elif estado == 46:
            token = TokenType.COMMENT
            lex += c
            estado = 0
            lex += "/"
            if (c == "\n"):
                lineno += 1

        # Detección de errores en la generación de tokens NUM, ID, o NOT_EQUAL_TO
        elif ((estado == 47 or estado == 48 or c == "!") and isError == True):
            errorPos = position
            isError = False
            if (c == "!"):
                errorType = 1

        elif estado == 999:
            token = TokenType.ERROR
            lex += c
            estado = 0
            position -= 1

        # Detección del token ENDFILE   
        elif estado == 1000:
            token = TokenType.ENDFILE
            lex = "$"
            print("Line:", lineno," ", token, lex)
        position += 1
        if estado != 0:
            lex += c

    # Se resta "uno" a el número de líneas al encontrar un token para evitar que este sea leído más
    # de una vez
    if (c == "\n"):
        lineno -= 1

    if (token != "" and token != TokenType.ENDFILE): 
            lex = str(lex)
            # Impresión del token y el lexema, así como la línea en que se encontró
            if (token != TokenType.ERROR):
                if (token != TokenType.ID or token != TokenType.NUM or token != TokenType.COMMENT):
                    print("Line:", lineno, " ", token, lex[:-1])
                else:
                    print("Line:", lineno," ", token, lex)
            else:
                # Impresión de la línea en que se encontró un error
                print("\n")
                if (lex[0].isdigit()):  
                    print("Line:",lineno, "ERROR al generar un token NUM")
                if (lex[0].isalpha()):
                    print("Line:",lineno, "ERROR al generar un token ID o palabra reservada")
                if (lex[0]=="!"):
                    print("Line:",lineno, "ERROR al generar un token NOT_EQUAL_TO")
                printError(lineno, errorPos, errorType)
            lex = ""
    # Se regresa el token y lexema
    return token, lex
            
        
