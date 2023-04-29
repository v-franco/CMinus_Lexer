# Realizado por:
# Juan Pablo Ortiz Ortega A01366969 
# Victor Hugo Franco Juárez A01366475

from globalTypes import *
from lexer import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math

firstCode = "" 
secondCode = ""
bagA = ""
bagB = ""
tokenBag = ""
dictA = {}
dictB = {}


#Función openCode abre ambos programas a comparar y los almacena en sus respectivas variables
def openCode(codeNo):
    global firstCode
    global secondCode
    #Abre programa 1 a revisar
    if codeNo == 1:
        f = open('program1.c-', 'r')
        programa = f.read() 		# lee todo el archivo a compilar
        f.close()
    #Abre programa 2 a revisar
    elif codeNo == 2: 
        f = open('program2.c-', 'r')
        programa = f.read() 		# lee todo el archivo a compilar
        f.close()
    #Variables usadas por el lexer
    progLong = len(programa) 
    programa = programa + '$' 	
    posicion = 0 			

    # función para pasar los valores iniciales de las variables globales
    globales(programa, posicion, progLong)


    #Usa el lexer para obtener todos los tokens de los programas y los almacena en sus respectivos strings
    token, tokenString = getToken(False)
    while (token != TokenType.ENDFILE):
        token, tokenString = getToken(False)
        if(codeNo) == 1:
            firstCode+=str(token)+" "
        elif(codeNo) == 2:
            secondCode+=str(token)+" "


#Función prepareTexts prepara los programas recibidos, generando una bolsa de palabras por cada programa y 
# un set con todos los tokens definidos en globalTypes
def prepareTexts():
    global bagA, bagB, firstCode, secondCode, tokenBag, dictA, dictB
    #Separa todos los tokens de los programas
    bagA = firstCode.split(' ') 
    bagB = secondCode.split(' ')
    #tokenBag = set(bagA).union(set(bagB))
    tokenBag = {"","TokenType.INT","TokenType.ENDFILE","TokenType.ERROR","TokenType.IF","TokenType.ELSE",
                "TokenType.RETURN","TokenType.VOID","TokenType.WHILE","TokenType.INPUT","TokenType.OUTPUT",
                "TokenType.ID", "TokenType.NUM", "TokenType.EQUAL_TO","TokenType.ASSIGN","TokenType.NOT_EQUAL_TO",
                "TokenType.LESS_THAN","TokenType.LESS_OR_EQUAL_TO","TokenType.MORE_THAN",
                "TokenType.MORE_OR_EQUAL_TO","TokenType.PLUS","TokenType.MINUS","TokenType.TIMES",
                "TokenType.SLASH","TokenType.LPAREN","TokenType.RPAREN","TokenType.LBRACKET","TokenType.RBRACKET",
                "TokenType.LCURLY","TokenType.RCURLY","TokenType.SEMI","TokenType.COMMENT","TokenType.COMMA"}
    
 
    #Llena los diccionarios con el no. de veces que aparece el token en cada programa
    dictA = dict.fromkeys(tokenBag, 0)
    for token in bagA:
        dictA[token]+=1

    dictB = dict.fromkeys(tokenBag, 0)
    for token in bagB:
        dictB[token]+=1
    
#Función TF calcula el TF de los programas. Recibe el diccionario generado en prepareTexts y la bolsa de palabras 
# del mismo programa. Regresa un diccionario con el TF.
def TF(dictionary, bag):
    tfDict = {} #Genera diccionario con el TF
    bagCount = len(bag)
    for token, count in dictionary.items():
        tfDict[token] = count / float(bagCount)
    return tfDict

#Función IDF calcula el IDF de los programas. Recibe los programas a utilizar. 
# Regresa un diccionario con el IDF.
def IDF(programs):
    N = len(programs)
    idfDict = {} #Genera el diccionario del IDF
    idfDict = dict.fromkeys(programs[0].keys(), 0)
    for program in programs:
        for token, value in program.items():
            if value > 0:
                idfDict[token] += 1
    for token, value in idfDict.items():
            idfDict[token] = (math.log(((1+N) / (1+float(value)))))+1 #+1 obtenido de scikit learn
    
    return idfDict

#Función TFIDF genera el TFIDF. recibe el TF del programa y los IDFs.
#Regresa el diccionario del TFIDF.
def TFIDF(tf, idfs):
    tfidf = {} #Genera el diccionario del TFIDF
    for token, value in tf.items():
        tfidf[token] = value * idfs[token]

    return tfidf


#Función helper dictToArray transforma un diccionario en un arreglo de numpy preparado para usarse 
# con scikit cosine_comparison. Recibe un diccionario, regresa un arreglo de numpy.  
def dictToArray(dictionary):

    dictList = list(dictionary.values())

    numpyArray = np.array([dictList])

    return numpyArray



#Función calculate genera la comparación de cosenos entre dos programas.
#Recibe el método a utilizar. 1 = TF-IDF, 2 = TF
#Imprime el resultado
def calculate(method):
    #Abre los códigos, prepara los textos
    openCode(1)
    openCode(2)
    prepareTexts()

    #Calcula los TF
    firstTF = TF(dictA, bagA)
    secondTF = TF(dictB, bagB)

    #Si method = 1, calcula el TF-IDF e imprime la comparación de cosenos usando TF-IDF
    if method == 1:
        idfs = IDF([dictA, dictB])

        firstTFIDF = TFIDF(firstTF, idfs)
        secondTFIDF = TFIDF(secondTF, idfs)

        finalArray1 = dictToArray(firstTFIDF)
        finalArray2 = dictToArray(secondTFIDF)


        cosine = cosine_similarity(finalArray1,finalArray2)

        print("Similaridad de coseno usando TF-IDF:",cosine)

    #Si method = 2, imprime la comparación de cosenos usando TF
    if method == 2:
        finalArray1 = dictToArray(firstTF)
        finalArray2 = dictToArray(secondTF)

        cosine = cosine_similarity(finalArray1,finalArray2)

        print("Similaridad de coseno usando TF:",cosine)    


def main():
    calculate(1)
    calculate(2)


if __name__ == "__main__":
    main()
