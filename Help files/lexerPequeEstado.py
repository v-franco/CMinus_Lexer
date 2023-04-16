s = "125+243.46   +  97.042+  25$"
blanco = ' \t\n'
digitos = '0123456789'

estado = 0
p = 0
lex = ''
token = ''

while (s[p] != '$' or (s[p]=='$' and estado != 0)) and estado != 7:
    c = s[p]
    if estado == 0:
        if c in blanco:
            estado = 0
            p += 1
        elif c in digitos:
            estado = 1
            lex += c
            p += 1
        elif c == '+':
            estado = 5
        elif c == '-':
            estado = 6
        else:
            estado = 7
    elif estado == 1:
        if c in digitos:
            estado = 1
            lex += c
            p += 1
        elif c == '.':
            estado = 3
            lex += c
            p += 1
        else:
            estado = 2
    elif estado == 2:
        token = 'INT'
        print(lex, token)
        estado = 0
        lex = ''
    elif estado == 3:
        if c in digitos:
            estado = 3
            lex += c
            p += 1
        else:
            estado = 4
    elif estado == 4:
        token = 'REAL'
        print(lex, token)
        estado = 0
        lex = ''
    elif estado == 5:
        token = 'PLUS'
        print('+', token)
        estado = 0
        lex = ''
        p += 1
    elif estado == 6:
        token = 'MINUS'
        print('-', token)
        estado = 0
        lex = ''
        p += 1
    elif estado == 7:
        # Se debe avanzar el puntero hasta un delimitador
        # colocar el estado = 0
        print('Error')
