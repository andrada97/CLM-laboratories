from nltk.tokenize import word_tokenize, casual_tokenize
import re

corpusName = "corpus.txt"
startWithBigLettter = "^([A-Z])"
listOfAbrv = ["Mr", "Dr", "Lect"]
listOfName = ["a priori", "San Francisco"]

def readCorpusFromFile(corpusName):
    file = open(corpusName,"r") 
    return file.read()

#Task 1
def tokenizeText(text):
    return casual_tokenize(text)

#Task 2
def checkIpAddresses(token):
    check = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",token)
    if(check):
        return True
    return False

def concatIpAddress(listOfTokens):
    newList = []
    index = 0
    while index < len(listOfTokens) :
        if index < len(listOfTokens)-2 and (checkIpAddresses(listOfTokens[index] + listOfTokens[index + 1])):
            newList.append(listOfTokens[index] + listOfTokens[index + 1])
            index = index + 1
        else:
            if index < len(listOfTokens)-3 and (checkIpAddresses(listOfTokens[index] + listOfTokens[index + 1] + listOfTokens[index + 2])):
                newList.append(listOfTokens[index] + listOfTokens[index + 1] + listOfTokens[index + 2])
                index = index + 2
            else:
                newList.append(listOfTokens[index])
            index = index + 1
    return newList


#Task 3       
def checkStartWith(token):
    #Verificare daca incepe cu litera mare
    return re.match(startWithBigLettter, token) or token in listOfAbrv
  
def checkForAbreviation(listOfTokens, index):
    return checkStartWith(listOfTokens[index]) and listOfTokens[index+1] == '.' and checkStartWith(listOfTokens[index+2])

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


####
def printList(listToPrint):
    for element in listToPrint:
        print(element)    

if __name__ == "__main__":
    
    listOfTokens = tokenizeText(readCorpusFromFile(corpusName))
    listOfTokens = concatIpAddress(listOfTokens)
    listOfTokens = concatNames(listOfTokens)
    printList(listOfTokens)
    
