import cPickle

from sklearn.feature_extraction.text import TfidfTransformer

import Playground.DudisPlayground.mtranslate.DB.ReadClassifyFromStorge


def classify(message):
    #read = ReadClassifyFromDB
    #clfDB = read.ReadFromDB('Harel')
    read = Playground.DudisPlayground.mtranslate.DB.ReadClassifyFromStorge
    clfDB = read.ReadClassifyFromStorge('HarelNew')
    clf = cPickle.loads(clfDB['classify'])
    TrainDataVector = cPickle.loads(clfDB['vector'])
    count_vect = cPickle.loads(clfDB['count'])
    #clf = cPickle.loads(clfDB[0][0])
    #TrainDataVector = cPickle.loads(clfDB[0][1])
    #count_vect = cPickle.loads(clfDB[0][2])
    testdata = [message]
    X_new_counts = count_vect.transform(testdata)
    tfidf_transformer = TfidfTransformer(use_idf=False).fit(TrainDataVector)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    for doc, category in zip(testdata, predicted):
       return (category)


x=classify("my storge ")
print x