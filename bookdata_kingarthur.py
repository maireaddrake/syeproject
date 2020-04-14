from sklearn.naive_bayes import MultinomialNB
import numpy as np
# from Processing import *
from dataprocessing import freq_words, data_writer, generate_y, combine, vectorize

# these are the two books
speakers = {0: 'knowles', 1: 'lowe'}

# get the data into np arrays
knowles_x = data_writer('knowles.txt')
knowles_y = generate_y(0, knowles_x)
lowe_x = data_writer('lowe.txt')
lowe_y = generate_y(1, lowe_x)

# combine data sets
books_x = combine(knowles_x, lowe_x)
books_y = combine(knowles_y, lowe_y)
# print(len(clinton_x))
# print(len(trump_x))

# get count vector and Tfidf transformer
vec, vect = vectorize(books_x)

# split data (50-50)
train_x = books_x[::2]
test_x = books_x[1::2]

train_y = books_y[::2]
test_y = books_y[1::2]

# train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(vect, books_y)

# estimate its accuracy
test_x = vec.transform(test_x)

predicted = clf.predict(test_x)

print("50/50 Prediction ratio:", np.mean(predicted == test_y))

# try a different split (80-20)
tx = []
ty = []
txt = []
tyt = []
for i in range(len(books_x)):
    if i % 5 == 0:
        txt.append(books_x[i])
        tyt.append(books_y[i])
    else:
        tx.append(books_x[i])
        ty.append(books_y[i])

# estimate its accuracy
txt = vec.transform(txt)
predicted = clf.predict(txt)

print("80/20 Prediction ratio:", np.mean(predicted == tyt))

# print(vect.shape)

# print most popular words
freq_words(vec, vect, 10)

# print("Prediction ratio 2:", np.mean(predicted == tyt))