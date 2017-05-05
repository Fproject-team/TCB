import base64
import cPickle


def classify():
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    import WriteClassifyToDB
    import ReadFromDB as train
    write = WriteClassifyToDB
    class TrainData:
        data = []
        target = []

    traindata = train.ReadFromDB('Harel')
    for i in traindata.data:
        i.decode().encode('utf-8').strip()
    count_vect = CountVectorizer()
    TrainDataVector = count_vect.fit_transform(traindata.data).toarray()
    clf = MultinomialNB().fit(TrainDataVector, traindata.target)
    write.WriteClassifyToDB('Harel',cPickle.dumps(clf))



x=classify()
