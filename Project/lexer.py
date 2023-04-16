from globalTypes import *

lineno = 1

def globales(prog, pos, long):
    global program
    global position
    global programLength
    program = prog
    position = pos
    programLength = long

def reservedLookup(tokenString):
    for w in ReservedWords:
        if tokenString == w.value:
            return TokenType(tokenString)
    return TokenType.ID


def getToken(imprime = True):
    global position, lineno
    tokenString = "" # string for storing token
    currentToken = None # is a TokenType value
    state = StateType.START # current state - always begins at START
    save = True # flag to indicate save to tokenString
    
    M = [[1,3,0,24,22,20,42,12,16,9,5,26,28,30,32,34,36,38,40,1000],
    [1,999,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [999,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
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
    [44,44,44,44,44,45,44,44,44,44,44,44,44,44,44,44,44,44,44,44],
    [44,44,44,44,44,44,46,44,44,44,44,44,44,44,44,44,44,44,44,44],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1000]]
    estado = 0
    lex = ''
    token = ''

    while (token == ""):
        c = program[position]
        if c.isdigit():
            col = 0
        elif c.isalpha():
            col = 1
        elif (c == ' ') or (c == '\t') or (c == '\n'):
            col = 2
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

 
        estado = M[estado][col]
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
            token = reservedLookup(lex[:-1])
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
        elif estado == 999:
            token = TokenType.ERROR
            lex += c
            estado = 0
        elif estado == 1000:
            token = TokenType.ENDFILE
            lex = "$"
            print("Line: ", lineno, token, lex)


        if (token != "" and token != TokenType.ENDFILE): 
            lex = str(lex)
            if (token != TokenType.ID or token != TokenType.NUM or token != TokenType.COMMENT):
                print("Line: ", lineno, token, lex[:-1])
                print("\n")
            else:
                print("Line: ", lineno, token, lex)
                print("\n")
            lex = ""
        position += 1
        if estado != 0:
            lex += c
        #print(lineno)

    return token, tokenString, lineno
            
        
