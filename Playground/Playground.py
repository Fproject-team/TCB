import sklearn

def PrintMyName( name ):
   "print my name and returns a name"
   print "My Name is:"
   print name
   return [name]

nnn = "Nimrod"
myName = "nimrod"

returnName = PrintMyName(myName)

print "The returned name is:"
print returnName

