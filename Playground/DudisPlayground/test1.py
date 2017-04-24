
from sklearn.feature_extraction.text import CountVectorizer
tags = [
  "dudi moran muli nimi","moran","muli"
]

dataset = [
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
target = [
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
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(dataset).toarray()
X_train_counts.shape
print (X_train_counts)

dataset1 = [
    "excel"
]

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_counts, target)
X_new_counts = count_vect.transform(dataset1)
tfidf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)

for doc, category in zip(dataset1, predicted):
    print((doc,category))