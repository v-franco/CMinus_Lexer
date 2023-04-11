M = [[1,7,5,6,0,7],[1,3,2,2,2,2],[0,0,0,0,0,0],[3,4,4,4,4,4],[0,0,0,0,0,0],
     [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
s = "125+243.46   +  97.042+  25$"
blanco = ' \t\n'
digitos = '0123456789'

estado = 0
p = 0
lex = ''
token = ''

while (s[p] != '$' or (s[p]=='$' and estado != 0)) and estado != 7:
    c = s[p]
    if c in digitos:
        col = 0
    elif c == '.':
        col = 1
    elif c == '+':
        col = 2
    elif c == '-':
        col = 3
    elif c in blanco:
        col = 4
    else:
        col = 5

    estado = M[estado][col]
    if estado == 2:
        token = 'INT'
        print(lex, token)
        lex = ''
        estado = 0
        p -= 1
    elif estado == 4:
        token = 'REAL'
        print(lex, token)
        lex = ''
        estado = 0
        p -= 1
    elif estado == 5:
        token = 'PLUS'
        print('+', token)
        lex = ''
        estado = 0
    elif estado == 6:
        token = 'MINUS'
        print('-', token)
        lex = ''
        estado = 0
    elif estado == 7:
        print("Error")
    p+=1
    if estado != 0:
        lex += c
        
