import cPickle

from sklearn.feature_extraction.text import TfidfTransformer

import ReadClassifyFromStorge


def classify(message):
    read = ReadClassifyFromStorge
    clfDB = read.ReadClassifyFromStorge('HarelNew')
    clf = cPickle.loads(clfDB['classify'])
    TrainDataVector = cPickle.loads(clfDB['vector'])
    count_vect = cPickle.loads(clfDB['count'])
    testdata = [message]
    X_new_counts = count_vect.transform(testdata)
    tfidf_transformer = TfidfTransformer(use_idf=False).fit(TrainDataVector)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    for doc, category in zip(testdata, predicted):
       return (category)

