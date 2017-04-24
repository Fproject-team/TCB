import BagOfWordsClass as bag
class Dictionary:
    dictionary=[]
    zeroList=[0]*len(dictionary)
    symbols=[]
####################################################################################
#this function get all symbols
    def Dictionary(self):
        self.getAllSymbols()
        self.load_words()


    def getAllSymbols(self):
        for symbolindex in range(33,65):
            self.symbols.append(chr(symbolindex))
        for symbolindex in range(123,126):
            self.symbols.append(chr(symbolindex))
        for symbolindex in range(91,96):
            self.symbols.append(chr(symbolindex))

#This function load words from file

    def load_words(self):
        file = open("bagOfWords.txt","r")
        tempString= file.read().lower().split(" ")
        for word in tempString:
            if(self.checkWordAndNoAdding(word)==False):
                self.dictionary.append(word)
        file.close()
        print "Load Finish"

    # This function save words to file
    def writeFile(self):
        file = open("bagOfWords.txt", "w+")
        for word in self.dictionary:
            file.write(word+" ")
        file.close()

#this function  get string, check all the words in the string' if in the dictioanry doesnt have this word, it will add it.
    def checkWord(self,string):
        spliter = string.split(" ")
        for word in spliter:
            inDictionary = False
            for index in self.dictionary:
                if (index == word.lower()):
                    print index +"-----> " + word
                    inDictionary=True
                    break
                else:
                    inDictionary = False
            if (inDictionary == False):
                word=self.check_Symbol_In_Word(word)
                self.dictionary.append(word.lower())

# this function  get word, and return TRUE if this word is already in the doctioanry
    def checkWordAndNoAdding(self,word):
        word.lower()
        inDictionary = False
        for index in self.dictionary:
            if (index== word):
                inDictionary = True
                indexWord = index;
                break
            else:
                inDictionary = False
        return inDictionary

# this function  get word, and return the index of this word
    def wordIndex(self,word):
        word.lower()
        counter=0
        for index in self.dictionary:
            if (word == index):
                return counter
            else:
                counter+=1
        if counter == len(self.dictionary):
            print "word not found in dictionary"

    # this function  create Vector
    def vectorCreate(self,string):
        tempString =string.split(" ")
        zeroList = [0] * len(self.dictionary)
        for word in tempString:
            word.lower()
            tempBool = self.checkWordAndNoAdding(word)
            if (tempBool == True):
                tempInt = self.wordIndex(word)
                zeroList[tempInt] += 1
        return zeroList

#Remove all symbols from words
    def check_Symbol_In_Word(self,word):
        for sym in self.symbols:
            word=word.replace(sym,"")
        return  word





#y=Dictionary()
'''

y.checkWord("dadi muli juni temp Muli")
print  y.dictionary
y.wordIndex("hwfijasdfsd")
arr= y.vectorCreate("muli muli temp")
print arr
'''
#y.getAllSymbols()
