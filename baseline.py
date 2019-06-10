import scraper as scp 
import pandas as pd 
import random
import collections
import math
import sys
from util import *
import re




d = pd.read_csv("completeDF.csv")

def featureExtractor(x):
    regex = re.compile('[^A-Za-z0-9]')

    sparse = collections.defaultdict(int)
    for i in x.split():
        text = regex.sub('', i)
        sparse[text] += 1
    return sparse


def linearPredictor(a, feature, numIters, eta):
    weights = {}
    for i in range(numIters):
        for i,j in a.iterrows():
            thing = feature(j['text'])
            vec = {}
            increment(vec, j['Top 100'], thing)
            dot = dotProduct(weights, vec)
            if dot < 1:
                increment(weights, eta, vec)
    return weights





a = d.loc[1:30000]
b = d.loc[30001:40000]

examples = [(j['text'],j['Top 100']) for i,j in b.iterrows()]
exam = [(j['text'],j['Top 100']) for i,j in a.iterrows()]

weights = linearPredictor(a, featureExtractor, 5, .4)
pri = evaluatePredictor(exam, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
print pri





