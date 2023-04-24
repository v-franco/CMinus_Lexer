# Realizado por:
# Juan Pablo Ortiz Ortega A01366969 
# Victor Hugo Franco Juárez A01366475

from globalTypes import *
from lexer import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from numpy.linalg import norm

firstText = ""
secondText = ""
bagA = ""
bagB = ""
unique = ""
dictA = {}
dictB = {}

def openCode(codeNo):
    global firstText
    global secondText
    #Abre programa 1 a revisar
    if codeNo == 1:
        f = open('program1.c-', 'r')
        programa = f.read() 		# lee todo el archivo a compilar
    elif codeNo == 2: 
        f = open('program2.c-', 'r')
        programa = f.read() 		# lee todo el archivo a compilar
    progLong = len(programa) 	# longitud original del programa
    programa = programa + '$' 	# agregar un caracter $ que represente EOF
    posicion = 0 			# posición del caracter actual del string

    # función para pasar los valores iniciales de las variables globales
    globales(programa, posicion, progLong)

    token, tokenString = getToken(False)
    while (token != TokenType.ENDFILE):
        token, tokenString = getToken(False)
        if(codeNo) == 1:
            firstText+=str(token)+" "
        elif(codeNo) == 2:
            secondText+=str(token)+" "


def prepareTexts():
    global bagA, bagB, firstText, secondText, unique, dictA, dictB
    bagA = firstText.split(' ')
    bagB = secondText.split(' ')
    unique = set(bagA).union(set(bagB))

    dictA = dict.fromkeys(bagA, 0)
    for token in bagA:
        dictA[token]+=1

    dictB = dict.fromkeys(bagB, 0)
    for token in bagB:
        dictB[token]+=1
    

def TF(dictionary, bag):
    tfDict = {}
    bagCount = len(bag)
    for token, count in dictionary.items():
        tfDict[token] = count / float(bagCount)
    return tfDict


def dictToArray(dictionary):

    dictList = list(dictionary.values())

    numpyArray = np.array(dictList)

    return numpyArray
    


def main():
    global firstText
    openCode(1)
    #print("First text saved:", firstText)
    openCode(2)
    #print("Second text saved:", firstText)
    prepareTexts()
    tf1 = TF(dictA, bagA)
    tf2 = TF(dictB, bagB)

    #print(tf1)
    #print(tf2)

    finalArray1 = dictToArray(tf1)
    finalArray2 = dictToArray(tf2)




    cosine = np.dot(finalArray1,finalArray2)/(norm(finalArray1)*norm(finalArray2))

    print(cosine)

    #VECTORES TIENEN QUE TENER EL MISMO TAMAÑO




if __name__ == "__main__":
    main()
