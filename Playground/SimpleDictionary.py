from array import array
indexWord=0
theDictionary = {}
zeroList=None




#This function check if the word is already in the dictionry,if not, the function add it
def checkWord(word):
    inDictionary=False
    for index in theDictionary:
        if(theDictionary[index] == word):
            inDictionary=True
            break
        else:
            inDictionary=False

    if(inDictionary == False):
        theDictionary[len(theDictionary)]=word.lower();

#This function check if the word is already in the dictionry
def checkWordAndNoAdding(word):
    word.lower()
    inDictionary = False
    for index in theDictionary:
        if (theDictionary[index] == word):
            inDictionary = True
            indexWord=index;
            break
        else:
            inDictionary = False
    return inDictionary

#This function split the string to words
def splitStringToWords(string):
    spliter=string.split(" ")
    return spliter

#Checking if the word is in the dictionary
def checkInDictionary(string):
    string = splitStringToWords(string)
    for iterator in string:
        checkWord(iterator)

def wordIndex(word):
    word.lower()
    for index in theDictionary:
        if(word == theDictionary[index]):
            return index

def wordsAmountInString(string):
    splitString = splitStringToWords(string)
    zeroList = [0] * len(theDictionary)
    for word in splitString:
        word.lower()
        tempBool=checkWordAndNoAdding(word)
        if(tempBool== True):
            tempInt=wordIndex(word)
            zeroList[tempInt]+=1
    return zeroList



string2 = "The icon opens but the icons do not appear in the program. Standard Dikla House of the Century, 21st Floor Permissions for the honeysuckle burst   The ININ permission and connection to the Peretz Forest must be opened, so you can enter the systemThanks The ININ does not openDuring the conversation I get another call (as if my status is vacant but actually I'm in a conversation) Call number 10069113 "

checkInDictionary(string2)
testArr=wordsAmountInString(string2)
print "this is the dictionary " ,theDictionary

string3= "TODO yosi icon  icon icon do not appear  House"
testArr=wordsAmountInString(string3)
#print theDictionary


print string3
print testArr