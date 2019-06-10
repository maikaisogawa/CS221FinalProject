import spotify as sp
import pandas as pd

df = pd.read_csv("realtot.csv")
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

#How to loop through the dataframe
for i, x in df.iterrows():
    songArtist = x['artist']
    songTitle = x['song']
    songId = sp.getSongId(songArtist, songTitle)
    obj = sp.getAudioFeatures(songId)
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

df.to_csv("allFeatures.csv")

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
