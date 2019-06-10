import pandas as pd 
import lyricsgenius
import random
import collections
import math
import time
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError




genius = lyricsgenius.Genius("rJlw4RGpYqaGwxCtW9Tif-o3j6SnXjXSX-_xZi_2Hs8NMmgW17ULodXCfHfGCXW_")

df = pd.read_csv("totTop100.csv")

dfnew = pd.DataFrame(columns = ['song', 'artist', 'text'])

lis = []

for i,x in df.iterrows():
    a = x['song']
    a = a.replace("F**k", "Fuck")
    a = a.replace("B****", "Bitch")
    a = a.replace("S**t", "Shit")
    a = a.replace("P****", "Pussy")
    a = a.replace("F*****g", "Fucking")
    a = a.replace("F***", "Fuck")
    
    tup = (a, x['artist'])
    


    lis.append((i,tup))

dff = []
def threadF(y):
    x = y[1]
    print(y[0])
    obj = {'song': x[0], 'artist':x[1], 'text': ""}
    a = None
    try:
        a = genius.search_song(x[0], x[1])
    except ConnectionError as e:    # This is the correct syntax
        print(e)
        r = "No response"
    
    time.sleep(5)
    if a:
        obj['text'] = a.lyrics
    dff.append(obj)


with ThreadPool(30) as threads:
    results = threads.map(threadF, lis[4001:8000])

for x in dff:
    dfnew = dfnew.append(x, ignore_index=True)

aaaa = dfnew.to_csv("testit9.csv")


""" print(0)
with ThreadPool(8) as threads:
    results = threads.map(threadF, lis[1001:1200])

for x in dff:
    dfnew = dfnew.append(x, ignore_index=True)

aaaa = dfnew.to_csv("testit2.csv")
print(1)

dfnew = pd.DataFrame(columns = ['song', 'artist', 'text'])

with ThreadPool(8) as threads:
    results = threads.map(threadF, lis[1201:1400])

for x in dff:
    dfnew = dfnew.append(x, ignore_index=True)

aaaa = dfnew.to_csv("testit2.csv")

print(2)
dfnew = pd.DataFrame(columns = ['song', 'artist', 'text'])

with ThreadPool(8) as threads:
    results = threads.map(threadF, lis[1401:1600])

for x in dff:
    dfnew = dfnew.append(x, ignore_index=True)

aaaa = dfnew.to_csv("testit2.csv")
print(3)
dfnew = pd.DataFrame(columns = ['song', 'artist', 'text'])

with ThreadPool(8) as threads:
    results = threads.map(threadF, lis[1601:1800])

for x in dff:
    dfnew = dfnew.append(x, ignore_index=True)

aaaa = dfnew.to_csv("testit2.csv")
print(4)

print(dfnew) """