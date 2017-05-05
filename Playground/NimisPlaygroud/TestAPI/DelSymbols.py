def getAllSymbols():
    sym =[]
    for symbolindex in range(33, 65):
        sym.append(chr(symbolindex))
    for symbolindex in range(123, 126):
        sym.append(chr(symbolindex))
    for symbolindex in range(91, 96):
        sym.append(chr(symbolindex))
    return sym


def check_Symbol_In_Word(word):
    symbols = getAllSymbols()
    for sym in symbols:
        word=word.replace(sym,"")
    return word
