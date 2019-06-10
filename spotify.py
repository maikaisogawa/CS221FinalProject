import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import random
# Basic setup
client_id = "1e9924def917464aa6ef63899e68e24e"
client_secret = "b094c129008c48a684345b3ffc50075c"

client_2 = "e26cbd7757204d14a4c63699e162b4a8"
secret_2 = "75941d50d22d472991d274ec61077813"

c_3 = "7097386ec6bc4fa782c01bdbbb03bc47"
s_3 = "55b3e6b7fa3a485fb92f865d597db123"

c_4 = "a22b51bb25964ec6886a91818e093cb3"
s_4 = "839827d8b8eb4ed7b8b5286f8793bcc0"

c_5 = "8ce0a0055fb445aea0baa77d0d85b6e2"
s_5 = "13dda8a821ef44499b6e763ba01045b5"

c_6 = "046397bea40d4a62bd0b5a54ba923f10"
s_6 = "2ad13a513beb479f8f5bcc042b9fa2b5"

a = random.randint(0,3)
if a < 1:
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
elif a < 2:
    client_credentials_manager = SpotifyClientCredentials(client_id=client_2, client_secret=secret_2)
else:
    client_credentials_manager = SpotifyClientCredentials(client_id=c_3, client_secret=s_3)

def getClientCreds():
    a = random.randint(0,5)
    if a < 1:
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    elif a < 2:
        client_credentials_manager = SpotifyClientCredentials(client_id=client_2, client_secret=secret_2)
    elif a < 3:
        client_credentials_manager = SpotifyClientCredentials(client_id=c_4, client_secret=s_4)
    elif a < 4:
        client_credentials_manager = SpotifyClientCredentials(client_id=c_5, client_secret=s_5)
    elif a < 5:
        client_credentials_manager = SpotifyClientCredentials(client_id=c_6, client_secret=s_6)
    else:
        client_credentials_manager = SpotifyClientCredentials(client_id=c_3, client_secret=s_3)

    return spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API



s_p = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API





### Returns Id for a specific song as string ###
# will return a 0 for songId if not found - account for this while coding algorithms to avoid errors 
def getSongId(artistName, trackName, sp = s_p):
    q = "artist:{} track:{}".format(artistName, trackName)
    #     format:"artist:%@ track:%@", artistName, trackName)
    # "Hello, {}. You are {}.".format(name, age)
    # q = String.init(format:"artist:%@ track:%@", artistName, trackName)
    songId = 0
    song = sp.search(q=q, type="track", limit=1)
    for i, t in enumerate(song['tracks']['items']):
        artistName = t['artists'][0]['name']
        trackName = t['name']
        songId = t['id']
        popularity = t['popularity']
    #print(songId)
    return songId

### Adds all audio features of a single song to dictionary - takes track ID as parameter ###
### returns object of particular song ###
def getAudioFeatures(trackId, sp = s_p):
    obj = None
    if trackId:

        features = sp.audio_features(str(trackId))
        if features[0]:

            duration_ms = features[0]['duration_ms']
            key = features[0]['key']
            acousticness = features[0]['acousticness']
            danceability = features[0]['danceability']
            energy = features[0]['energy']
            instrumentalness = features[0]['instrumentalness']
            liveness = features[0]['liveness']
            loudness = features[0]['loudness']
            speechiness = features[0]['speechiness']
            tempo = features[0]['tempo']
            valence = features[0]['valence']

            obj = {
                "id": str(trackId),
                "duration_ms": duration_ms,
                "key": key,
                "acousticness": acousticness,
                "danceability": danceability,
                "energy": energy,
                "instrumentalness": instrumentalness,
                "liveness": liveness,
                "loudness": loudness,
                "speechiness": speechiness,
                "tempo": tempo,
                "valence": valence
            }

        return obj if obj else None
    #songData[title] = obj

# songData = {}  # dictionary: key is song title, value is all metadata

# single example
""" songArtist = 'ABBA'
songTitle = 'Dancing Queen'
songId = getSongId(songArtist, songTitle)
#getAudioFeatures(songId, songTitle)
print(songData) """

############## OTHER FUNCTIONS NOT YET IMPLEMENTED ######################

# #Extract Artist's uri
# artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
# #Pull all of the artist's albums
# sp_albums = sp.artist_albums(artist_uri, album_type='album')
# #Store artist's albums' names' and uris in separate lists
# album_names = []
# album_uris = []
# for i in range(len(sp_albums['items'])):
#     album_names.append(sp_albums['items'][i]['name'])
#     album_uris.append(sp_albums['items'][i]['uri'])
    
# album_names
# album_uris
# #Keep names and uris in same order to keep track of duplicate albums

# # ### Grab songs from each album ###
# # def albumSongs(uri):
# #     album = uri #assign album uri to a_name
# # spotify_albums[album] = {} #Creates dictionary for that specific album
# # #Create keys-values of empty lists inside nested dictionary for album
# #     spotify_albums[album]['album'] = [] #create empty list
# #     spotify_albums[album]['track_number'] = []
# #     spotify_albums[album]['id'] = []
# #     spotify_albums[album]['name'] = []
# #     spotify_albums[album]['uri'] = []
# # tracks = sp.album_tracks(album) #pull data on album tracks
# # for n in range(len(tracks['items'])): #for each song track
# #         spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
# #         spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
# #         spotify_albums[album]['id'].append(tracks['items'][n]['id'])
# #         spotify_albums[album]['name'].append(tracks['items'][n]['name'])
# #         spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])

# ### Store album data ###
# # spotify_albums = {}
# # album_count = 0
# # for i in album_uris: #each album
# #     albumSongs(i)
# #     print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums dictionary")
# #     album_count+=1 #Updates album count once all tracks have been added

# ### Grab audio features for each song ###
# def audio_features(album):
#     #Add new key-values to store audio features
#     spotify_albums[album]['acousticness'] = []
#     spotify_albums[album]['danceability'] = []
#     spotify_albums[album]['energy'] = []
#     spotify_albums[album]['instrumentalness'] = []
#     spotify_albums[album]['liveness'] = []
#     spotify_albums[album]['loudness'] = []
#     spotify_albums[album]['speechiness'] = []
#     spotify_albums[album]['tempo'] = []
#     spotify_albums[album]['valence'] = []
#     spotify_albums[album]['popularity'] = []
#     #create a track counter
#     track_count = 0
#     for track in spotify_albums[album]['uri']:
#         #pull audio features per track
#         features = sp.audio_features(track)
        
#         #Append to relevant key-value
#         spotify_albums[album]['acousticness'].append(features[0]['acousticness'])
#         spotify_albums[album]['danceability'].append(features[0]['danceability'])
#         spotify_albums[album]['energy'].append(features[0]['energy'])
#         spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
#         spotify_albums[album]['liveness'].append(features[0]['liveness'])
#         spotify_albums[album]['loudness'].append(features[0]['loudness'])
#         spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
#         spotify_albums[album]['tempo'].append(features[0]['tempo'])
#         spotify_albums[album]['valence'].append(features[0]['valence'])
#         #popularity is stored elsewhere
#         pop = sp.track(track)
#         spotify_albums[album]['popularity'].append(pop['popularity'])
#         track_count+=1


# ### Loop through extracting audio features ###
# # add time request to avoid over-pinging Spotify servers
# import time
# import numpy as np
# sleep_min = 2
# sleep_max = 5
# start_time = time.time()
# request_count = 0
# for i in spotify_albums:
#     audio_features(i)
#     request_count+=1
#     if request_count % 5 == 0:
#         print(str(request_count) + " playlists completed")
#         time.sleep(np.random.uniform(sleep_min, sleep_max))
#         print('Loop #: {}'.format(request_count))
#         print('Elapsed Time: {} seconds'.format(time.time() - start_time))

# # add data to new dataframe #
# dic_df = {}
# dic_df['album'] = []
# dic_df['track_number'] = []
# dic_df['id'] = []
# dic_df['name'] = []
# dic_df['uri'] = []
# dic_df['acousticness'] = []
# dic_df['danceability'] = []
# dic_df['energy'] = []
# dic_df['instrumentalness'] = []
# dic_df['liveness'] = []
# dic_df['loudness'] = []
# dic_df['speechiness'] = []
# dic_df['tempo'] = []
# dic_df['valence'] = []
# dic_df['popularity'] = []
# for album in spotify_albums: 
#     for feature in spotify_albums[album]:
#         dic_df[feature].extend(spotify_albums[album][feature])
        
# len(dic_df['album'])

# # convert to dataframe

# import pandas as pd
# df = pd.DataFrame.from_dict(dic_df)
# df

# # remove duplicates
# print(len(df))
# final_df = df.sort_values('popularity', ascending=False).drop_duplicates('name').sort_index()
# print(len(final_df))

# # save to csv
# final_df.to_csv("/Users/maikaisogawa/Downloads")