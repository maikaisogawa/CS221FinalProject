import pandas as pd 
import random
import collections
import math

""" d_1 = pd.read_csv("naaaahing.csv")
d_2 = pd.read_csv("naaaahing_2.csv")
d_3 = pd.read_csv("naaaahing_3.csv")
d_4 = pd.read_csv("naaaahing_4.csv")
d_5 = pd.read_csv("naaaahing_5.csv")
d_6 = pd.read_csv("naaaahing_6.csv")
d_7 = pd.read_csv("naaaahing_7.csv")

df = d_1
df = df.append(d_2)
df = df.append(d_3)
df = df.append(d_4)
df = df.append(d_5)
df = df.append(d_6)
df = df.append(d_7)


df.to_csv("top100total.csv") """

#d = pd.read_csv("top100total.csv")
#print(len(d))

oldset = pd.read_csv("completeDF.csv")
df = pd.DataFrame(columns = ['X1', 'artist', 'song', 'link', 'text', 'Top 100'], dtype= str)

samp = oldset.sample(n = 5100)

for i,x in samp.iterrows():
    if(x['Top 100'] == -1):
        x['Top 100'] = 'No'
        df = df.append(x)


dif = pd.read_csv("top100total.csv") 
dif = dif.append(df)

dif.to_csv("totalsample.csv")





