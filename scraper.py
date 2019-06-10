import pandas as pd 
from sets import Set


d = pd.read_csv("songdata.csv")
thing = pd.read_csv("thing.csv")

s = Set()

for i,x in thing.iterrows():
    s.add((x['Song Title'], x['Artist'])) 
a = []

for i,x in d.iterrows():
    new_x = (x['song'], x['artist'])
    if new_x in s:
        a.append(1)
    else:
        a.append(-1)

d['Top 100'] = a

exp = d.to_csv('completeDF.csv')