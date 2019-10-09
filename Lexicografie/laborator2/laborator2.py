from nltk.tokenize import word_tokenize, casual_tokenize
import re

corpusName = "corpus.txt"
startWithBigLettter = "^([A-Z])"
listOfAbrv = ["Mr", "Dr", "Lect"]
listOfName = ["a priori", "San Francisco"]

def readCorpusFromFile(corpusName):
    file = open(corpusName,"r") 
    return file.read()
def tokenizeText(text):
    return casual_tokenize(text)

def checkStartWith(token):
    return re.match(startWithBigLettter, token) or token in listOfAbrv

def concatNames(listOfTokens):
    newList = []
    index = 0
    while index< len(listOfTokens):
        if index <=len(listOfTokens)-3 and checkForAbreviation(listOfTokens, index):
                newList.append(listOfTokens[index] + listOfTokens[index+1] + " "+ listOfTokens[index+2])
                index = index +2
        else:
            newList.append(listOfTokens[index])
        index = index +1
    return newList        
            
def checkForAbreviation(listOfTokens, index):
    return checkStartWith(listOfTokens[index]) and listOfTokens[index+1] == '.' and checkStartWith(listOfTokens[index+2])



####
def printList(listToPrint):
    for element in listToPrint:
        print(element)    

if __name__ == "__main__":
    
    listOfTokens = tokenizeText(readCorpusFromFile(corpusName))
    listOfTokens = concatNames(listOfTokens)
    printList(listOfTokens)
    