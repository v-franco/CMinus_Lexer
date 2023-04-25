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
mixedBag = ""
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
    #Abre programa 2 a revisar
    elif codeNo == 2: 
        f = open('program2.c-', 'r')
        programa = f.read() 		# lee todo el archivo a compilar

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


#Función prepareTexts prepara los programas recibidos, generando una bolsa de palabras por cada programa, una bolsa con todos los tokens de ambos programas
def prepareTexts():
    global bagA, bagB, firstCode, secondCode, mixedBag, dictA, dictB
    bagA = firstCode.split(' ')
    bagB = secondCode.split(' ')
    #mixedBag = set(bagA).union(set(bagB))
    mixedBag = {"","TokenType.INT","TokenType.ENDFILE","TokenType.ERROR","TokenType.IF","TokenType.ELSE","TokenType.RETURN","TokenType.VOID","TokenType.WHILE","TokenType.INPUT","TokenType.OUTPUT","TokenType.ID", "TokenType.NUM", "TokenType.EQUAL_TO","TokenType.ASSIGN","TokenType.NOT_EQUAL_TO","TokenType.LESS_THAN","TokenType.LESS_OR_EQUAL_THAN","TokenType.MORE_THAN","TokenType.MORE_OR_EQUAL_THAN","TokenType.PLUS","TokenType.MINUS","TokenType.TIMES","TokenType.SLASH","TokenType.LPAREN","TokenType.RPAREN","TokenType.LBRACKET","TokenType.RBRACKET","TokenType.LCURLY","TokenType.RCURLY","TokenType.SEMI","TokenType.COMMENT","TokenType.COMMA","TokenType.CLOSE_COMMENT"}
    #print(mixedBag)
    dictA = dict.fromkeys(mixedBag, 0)
    for token in bagA:
        dictA[token]+=1

    dictB = dict.fromkeys(mixedBag, 0)
    for token in bagB:
        dictB[token]+=1
    

def TF(dictionary, bag):
    tfDict = {}
    bagCount = len(bag)
    for token, count in dictionary.items():
        tfDict[token] = count / float(bagCount)
    return tfDict


def IDF(programs):
    N = len(programs)
    idfDict = {}
    idfDict = dict.fromkeys(programs[0].keys(), 0)
    for program in programs:
        for token, value in program.items():
            if value > 0:
                idfDict[token] += 1
    for token, value in idfDict.items():
        idfDict[token] = math.log((1+N / 1+float(value))+1)
    
    return idfDict

def TFIDF(tfBag, idfs):
    tfidf = {}
    for token, value in tfBag.items():
        tfidf[token] = value * idfs[token]

    return tfidf


def dictToArray(dictionary):

    dictList = list(dictionary.values())

    numpyArray = np.array([dictList])

    return numpyArray


def calculateTFIDF():
    global firstCode
    openCode(1)
    openCode(2)
    prepareTexts()
    firstTF = TF(dictA, bagA)
    secondTF = TF(dictB, bagB)

    idfs = IDF([dictA, dictB])

    firstTFIDF = TFIDF(firstTF, idfs)
    secondTFIDF = TFIDF(secondTF, idfs)

    finalArray1 = dictToArray(firstTFIDF)
    finalArray2 = dictToArray(secondTFIDF)


    cosine = cosine_similarity(finalArray1,finalArray2)

    print("Similaridad de coseno usando TF-IDF:",cosine)

def calculateTF():
    global firstCode
    openCode(1)

    openCode(2)

    prepareTexts()
    firstTF = TF(dictA, bagA)
    secondTF = TF(dictB, bagB)

    finalArray1 = dictToArray(firstTF)
    finalArray2 = dictToArray(secondTF)


    cosine = cosine_similarity(finalArray1,finalArray2)

    print("Similaridad de coseno usando TF:",cosine)


def main():
    calculateTFIDF()
    calculateTF()


if __name__ == "__main__":
    main()
