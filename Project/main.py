from globalTypes import *
from lexer import *


#sample.c-
fileName = "test1"
f = open(fileName + '.c-', 'r')
programa = f.read() 		# lee todo el archivo a compilar
f.close()                       # cerrar el archivo con programa fuente
progLong = len(programa) 	# longitud original del programa
programa = programa + '$' 	# agregar un caracter $ que represente EOF
posicion = 0 			# posición del caracter actual del string

# Para probar el scanner solito
globales(programa, posicion, progLong) # para mandar los globales

token, tokenString, _ = getToken()
while (token != TokenType.ENDFILE):
    token, tokenString, _ = getToken()
