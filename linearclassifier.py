import pandas as pd
import random
import collections
import math
import sys
from util import *
import re
import sklearn
import numpy as np

# Import the data
d0 = pd.read_csv("finalPLEASE.csv")
d = d0.drop(d0.columns[0], axis = 1)
# Data preprocessing: specify our training and test data
colname = [col for col in d]
colname.remove('Top 100')
colname.remove('artist')
colname.remove('song')

d1 = d.drop('Top 100', axis = 1)
# lyrics = [j['text'] for i,j in attributes.iterrows()]         # X
# label = []
# for i,j in d.iterrows():
#     label.append()
label = [1 if j['Top 100'] == 'Yes' else -1 for i,j in d.iterrows()]       # y

attribute = list()
for i,j in d1.iterrows():
    feature = dict()
    for col in colname:
        feature[col] = j[col]
    attribute.append(feature)

# Splitting the data into Train and Testing examples
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(attribute, label, test_size=0.20, random_state=42)
# print len(X_test)
# print len(X_train)
# print X_train.loc[:, "artist"]

# reconstruct our training and test data
trainexamples = [(X_train[i], y_train[i]) for i in range(len(X_train))]
testexamples = [(X_test[i], y_test[i]) for i in range(len(X_test))]

print trainexamples[0]
# print trainexamples[0:5]

# our new featureExtractor that extracts all features into one feature vector
def featureExtractor(d):
    sparse = collections.defaultdict(float)
    regex = re.compile('[^A-Za-z0-9]')
    for key in d:
        if key == 'text':
            for i in d[key].split():
                text = regex.sub('', i)
                sparse[text] += 1
        else:
            sparse[key] = d[key]
    return sparse


# Our linear predictor: gives the trained weights dictionary
# examples are array of dictionary: [{text: ''}, {d2}]
def linearPredictor(examples, feature, numIters, eta):
    weights = collections.defaultdict(float)
    for n in range(numIters):
        for i,j in examples:
            features = feature(i)
            identity = dotProduct(weights, features) * j
            I = -1 if identity < 1 else 0
            increment(weights, -eta * I * j, features)
    return weights


# def linearPredictor(examples, feature, numIters, eta):
#     weights = {}
#     for k in range(numIters):
#         for i,j in examples:
#             thing = feature(i)
#             vec = {}
#             increment(vec, j, thing)
#             dot = dotProduct(weights, vec)
#             if dot < 1:
#                 increment(weights, eta, vec)
#     return weights


# Train the weights using training examples
weights = linearPredictor(trainexamples, featureExtractor, 5, .4)
# Predict using binary linear classifier with the test examples
def predict(examples, predictor):
    prediction = [predictor(x) for x,y in examples]
    return prediction

# Predict using the trained weights
predictorfunction = lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1)
y_true = [top100 for text,top100 in testexamples]
y_pred = predict(testexamples, predictorfunction)

# Output the metrics: confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
print 'The confusion matrix is: '
print cm

# Output the metrics: accuracy score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)
print 'The accuracy of the linear classifier is {} .'.format(accuracy)

# Output the metrics: F1_score
from sklearn.metrics import f1_score
f1 = f1_score(y_true, y_pred, average = 'binary')
print 'The F1 score of the linear classifier is {} .'.format(f1)
