from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
def classify(message):
    count_vect = CountVectorizer()
    testdata = [message]
    X_new_counts = count_vect.transform(testdata)
    tfidf_transformer = TfidfTransformer(use_idf=False).fit(TrainDataVector)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    for doc, category in zip(testdata, predicted):
        return (category)