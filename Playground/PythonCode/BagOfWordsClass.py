class BagOfWords:
    bag_of_words = []

################################################################################################



#This function load words from file,this function will activited at start
    def load_words(self):
        file = open("bagOfWords.txt","r")
        tempString= file.read().lower().split(" ")
        for word in tempString:
            self.bag_of_words.append(word)

        file.close()
        print "Load Finish"


#Print all the words in the bag
    def printBagOfWords(self):
        for index in self.bag_of_words:
            print index

#Save words to file,this function will activate in the end of the main






    def getBag_of_words(self):
        return self.bag_of_words

    def insertWord(self,word):
        num=len(self.bag_of_words)
        print num
        self.bag_of_words.append(word)

    def getWord(self,number):
        return self.bag_of_words[number]

    def returnWordIndex(self,word):
        counter=0;
        for num in self.bag_of_words:
            if num==word:
                return counter
            else:
                counter+=1


    def insertString(self,string):
        spliter = string.split(" ")
        for word in spliter:
            self.bag_of_words.append(word)

####################### Test Functions ###################
'''
x=BagOfWords()#V
x.load_words()#V
x.printBagOfWords()#V
temp =x.getBag_of_words()#V
#x.insertString("muli dudi sham shay")
x.printBagOfWords()
print x.returnWordIndex("sham")
x.writeFile()
'''