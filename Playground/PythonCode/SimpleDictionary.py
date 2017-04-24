############################################# Imports #############################################


from array import array
from sklearn.feature_extraction.text import CountVectorizer
import DictionaryC as dic


############################################# Varibles #############################################
indexWord=0
theDictionary = {}
zeroList=None
y=dic.Dictionary()

############################################# Functions #############################################

string2 = "The^ icon#$ !@#opens ^&^&but the icons do not appear in the program. Standard Dikla House of the Century, 21st Floor Permissions for the honeysuckle burst   The ININ permission and connection to the Peretz Forest must be opened, so you can enter the systemThanks The ININ does not openDuring the conversation I get another call (as if my status is vacant but actually I'm in a conversation) Call number 10069113 "
string3= "TODO yosi icon  icon icon do not appear  House"
string4= "muli Muli MuLi Limu"

############################################# Main #############################################

y.Dictionary()
print y.symbols
y.checkWord(string2)
print y.dictionary

print y.vectorCreate("muli test numet it the to")