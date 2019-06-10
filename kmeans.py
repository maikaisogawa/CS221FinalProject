import numpy as np 
from sklearn.cluster import KMeans
import pandas as pd 

df = pd.read_csv("finalspotify2.csv")
df = df.drop(columns = ['song', 'artist', 'X1', 'Top 100', 'text', 'duration_ms'], axis = 1)

arr = []

for i,x in df.iterrows():
    if not pd.isnull(x['key']):
        y = x.to_numpy()
        arr.append(y)

arr = np.array(arr)

kmeans = KMeans(n_clusters=2, random_state=0).fit(arr)
print(kmeans.cluster_centers_)