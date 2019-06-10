import pandas as pd 

df = pd.read_csv("finalspotify1.csv")


lis = []

df2 = pd.read_csv("check2.csv")

for i,x in df2.iterrows():
    if x['Top 100'] != 'Yes':
        lis.append(x)



for i in lis:
    df = df.append(i)


aaa = df.to_csv("finalspotify2.csv")