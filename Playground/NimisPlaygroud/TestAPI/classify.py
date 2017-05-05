SYMBOLS = '~!@#%^?"${}()[].,:;+-*/&|<>=~1234567890'
def myFunction(exList):
    result = map(lambda Element: Element.translate(None, SYMBOLS).strip(), exList)
    return result
def classify(message):
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    import ReadFromDB as train
    import DelSymbols as Sym
    class TrainData:
        data = []
        target = []

    oldtraindata = TrainData()
    oldtraindata.data = [
        "I don't have internet",
        "the light is broken",
        "My paycheck is wrong",
        "my computer didn't start",
        "my phone doesn't work",
        "the table is broken",
        "the chair is not working",
        "my keyboard is missing a key",
        "I didn't get my salary this month",
        "where can I find the expense report",
        "how much an i changed for my car",
        "what is my yearly budget",
        "I can't open excel"
    ]
    oldtraindata.target = [
        "IT",
        "Maintenance",
        "Finance",
        "IT",
        "IT",
        "Maintenance",
        "Maintenance",
        "IT",
        "Finance",
        "Finance",
        "Finance",
        "Finance",
        "IT"
    ]
    traindata = train.ReadFromDB()
    for i in traindata.data:
        i = myFunction(i)
    print traindata.data
    testdata = [message]
    count_vect = CountVectorizer()
    TrainDataVector = count_vect.fit_transform(traindata.data).toarray()
    clf = MultinomialNB().fit(TrainDataVector, traindata.target)
    X_new_counts = count_vect.transform(testdata)
    tfidf_transformer = TfidfTransformer(use_idf=False).fit(TrainDataVector)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    for doc, category in zip(testdata, predicted):
        return (category)


x=classify("cant open computer")
print(x)