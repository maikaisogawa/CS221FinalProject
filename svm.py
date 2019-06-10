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
# lyrics = [j['text'] for i,j in attribute.iterrows()]         # X
# label = []
# for i,j in d.iterrows():
#     label.append()
label = [1.0 if j['Top 100'] == 'Yes' else -1.0 for i,j in d.iterrows()]       # y

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
# trainexamples = [(X_train[i], y_train[i]) for i in range(len(X_train))]
# testexamples = [(X_test[i], y_test[i]) for i in range(len(X_test))]

# print trainexamples[0]
# print trainexamples[0:5]

# our new featureExtractor that extracts all features into one feature vector
def featureExtractor(d):
    sparse = collections.defaultdict(int)
    regex = re.compile('[^A-Za-z0-9]')
    for key in d:
        if key == 'text':
            for i in d[key].split():
                text = regex.sub('', i)
                sparse[text] += 1
        else:
            sparse[key] = d[key]
    return sparse

# def zerofeature(d):
#     sparse = collections.defaultdict(int)
#     regex = re.compile('[^A-Za-z0-9]')
#     for key in d:
#         if key == 'text':
#             for i in d[key].split():
#                 text = regex.sub('', i)
#                 sparse[text] = 0.0
#         else:
#             sparse[key] = 0.0
#     return sparse

# math.log10(X)
# bool means if it is training data
def generateSparse(examples, feature):          # want m*10000
    sparse = []
    for j in examples:
        # if bool and j in X_test:
        #     sparse.append(zerofeature(j))
        # elif bool != True and j in X_train:
        #     sparse.append(zerofeature(j))
        # else:
        sparse.append(feature(j))
    return sparse

trainsparse = generateSparse(X_train, featureExtractor)
testsparse = generateSparse(X_test, featureExtractor)

# trainsparse = generateSparse(attribute, featureExtractor, zerofeature, True)
# testsparse = generateSparse(attribute, featureExtractor, zerofeature, False)

# print len(trainsparse)
# print len(testsparse)


# # print trainsparse[0:5]
# # print y_train
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
trainmatrix = vec.fit_transform(trainsparse)
testmatrix = vec.transform(testsparse)

# SVM - try linear, polynomial, rbf, sigmoid kernal function with SVC
from sklearn.svm import SVC
svclassifier = SVC(kernel = 'linear')
svclassifier.fit(trainmatrix, y_train)
y_pred = svclassifier.predict(testmatrix)

# python svm.py
y_true = y_test

# Output the metrics: confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
print 'The confusion matrix is: '
print cm

# Output the metrics: accuracy score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)
print 'The accuracy of the linear svc is {} .'.format(accuracy)

# Output the metrics: F1_score
from sklearn.metrics import f1_score
f1 = f1_score(y_true, y_pred, average = 'binary')
print 'The F1 score of the linear svc is {} .'.format(f1)

############################################
# polynomial
svclassifier_poly = SVC(kernel = 'poly', degree = 8)
svclassifier_poly.fit(trainmatrix, y_train)
y_pred_poly = svclassifier_poly.predict(testmatrix)

cm_poly = confusion_matrix(y_true, y_pred_poly)
print 'The confusion matrix is: '
print cm_poly

accuracy_poly = accuracy_score(y_true, y_pred_poly)
print 'The accuracy of the polynomial svc is {} .'.format(accuracy_poly)

f1_poly = f1_score(y_true, y_pred_poly, average = 'binary')
print 'The F1 score of the polynomial svc is {} .'.format(f1_poly)

###############################################
# Guassian
svclassifier_rbf = SVC(kernel = 'rbf')
svclassifier_rbf.fit(trainmatrix, y_train)
y_pred_rbf = svclassifier_rbf.predict(testmatrix)

cm_rbf = confusion_matrix(y_true, y_pred_rbf)
print 'The confusion matrix is: '
print cm_rbf

accuracy_rbf = accuracy_score(y_true, y_pred_rbf)
print 'The accuracy of the Guassian svc is {} .'.format(accuracy_rbf)

f1_rbf = f1_score(y_true, y_pred_rbf, average = 'binary')
print 'The F1 score of the Guassian svc is {} .'.format(f1_rbf)

#############################################
# Sigmoid Kernel
svclassifier_sgd = SVC(kernel = 'sigmoid')
svclassifier_sgd.fit(trainmatrix, y_train)
y_pred_sgd = svclassifier_rbf.predict(testmatrix)

cm_sgd = confusion_matrix(y_true, y_pred_sgd)
print 'The confusion matrix is: '
print cm_sgd

accuracy_sgd = accuracy_score(y_true, y_pred_sgd)
print 'The accuracy of the Sigmoid SVC is {} .'.format(accuracy_sgd)

f1_sgd = f1_score(y_true, y_pred_sgd, average = 'binary')
print 'The F1 score of the Sigmoid SVC is {} .'.format(f1_sgd)
