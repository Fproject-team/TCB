
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform("testdoc.doc".__doc__)
X_train_counts.shape
count_vect.vocabulary_.get(u'algorithm')