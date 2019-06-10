import spotify as sp
import pandas as pd
import time
import numpy as np
from multiprocessing.pool import ThreadPool
import random
from requests.exceptions import ConnectionError
import requests


df = pd.read_csv("conglom.csv")
#Add columns to the dataframe following format below
df['duration_ms'] = None
df['key'] = None
df['acousticness'] = None
df['danceability'] = None
df['energy'] = None
df['instrumentalness'] = None
df['liveness'] = None
df['loudness'] = None
df['speechiness'] = None
df['tempo'] = None
df['valence'] = None

sleepmin = 2
sleepmax = 5
count = 0

thing = []

def threadF(y):
    aaaa = sp.getClientCreds()

    global thing
    x = y[1]
    time.sleep(1)
    songArtist = x['artist']
    songTitle = x['song']
    songArtist = songArtist.split("Featuring")[0]
    songArtist = songArtist.split("&")[0]
    obj = None
    try:
        songId = sp.getSongId(songArtist, songTitle, sp = aaaa)
        obj = sp.getAudioFeatures(songId, sp = aaaa)
    except requests.exceptions.RequestException as e:    # This is the correct syntax
        print(e)
        r = "No response"


    print(y[0])
    if obj:
        x['duration_ms'] = obj['duration_ms']
        x['key'] = obj['key']
        x['acousticness'] = obj['acousticness']
        x['danceability'] = obj['danceability']
        x['energy'] = obj['energy']
        x['instrumentalness'] = obj['instrumentalness']
        x['liveness'] = obj['liveness']
        x['loudness'] = obj['loudness']
        x['speechiness'] = obj['speechiness']
        x['tempo'] = obj['tempo']
        x['valence'] = obj['valence']
    thing.append(x)

with ThreadPool(8) as threads:
    results = threads.map(threadF, df[6001:7600].iterrows())


df2 = df[0:0]

for a in thing:
    df2 = df2.append(a)



df2.to_csv("firstspotify7.csv")

import pandas as pd
df = pd.read_csv("firstspotify.csv")
df2 = pd.read_csv("firstspotify2.csv")
df3 = pd.read_csv("firstspotify3.csv")
df4 = pd.read_csv("firstspotify4.csv")
df5 = pd.read_csv("firstspotify5.csv")
df6 = pd.read_csv("firstspotify6.csv")
df7 = pd.read_csv("firstspotify7.csv")



# #How to loop through the dataframe
# for i, x in df.iterrows():
#     if i % 500:
#         time.sleep(1)
#     songArtist = x['artist']
#     songTitle = x['song']
#     songId = sp.getSongId(songArtist, songTitle)
#     obj = sp.getAudioFeatures(songId)
#     #print(obj)
#     print(i)
#     if obj:
#         x['duration_ms'] = obj['duration_ms']
#         x['key'] = obj['key']
#         x['acousticness'] = obj['acousticness']
#         x['danceability'] = obj['danceability']
#         x['energy'] = obj['energy']
#         x['instrumentalness'] = obj['instrumentalness']
#         x['liveness'] = obj['liveness']
#         x['loudness'] = obj['loudness']
#         x['speechiness'] = obj['speechiness']
#         x['tempo'] = obj['tempo']
#         x['valence'] = obj['valence']






# #Add columns to the dataframe following format below
# df['Column Name'] = None
# #loop through later to actually add values

# #How to loop through the dataframe
# for i,x in df.iterrows():
#     #i is row index
#     #x is entire row
#     #x['column name'] will give you the value of that column in that row
#     return


# oldset = pd.read_csv("realtot.csv")
# df = pd.DataFrame(columns = ['X1', 'Top 100', 'artist', 'song', 'text', 'duration_ms', 'key', 'acousticness', 
#     'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence'], dtype= str)

# samp = oldset.sample(n = 5100)

# for i, x in oldset.iterrows():

#     if(x['Top 100'] == -1):
#         x['Top 100'] = 'No'
#         df = df.append(x)
