import pandas as pd 
import lyricsgenius
import random
import collections
import math
import time
from multiprocessing.pool import ThreadPool

df = pd.read_csv("check2.csv")

''' [('Aba Daba Honeymoon', 'Debbie Reynolds and Carleton Carpenter'), ("You're Just In Love", 'Perry Como and The Fontane Sisters'), ('Wish You Were Here', 'Eddie Fisher and Hugo Winterhalter'), ('Mercy', 'Kanye West, Big Sean, Pusha T, 2 Chainz'), ("Boys 'Round Here", 'Blake Shelton feat. Pistol Annies and Friends'), ('Bad', 'Wale feat. Tiara Thomas or Rihanna')]



[ , ("Limelight (Terry's Theme)", 'Frank Chacksfield'), ('Fascination', 'Jane Morgan and the Troubadours'), ('Moritat', 'Richard Hayman and Jan August'), ('Canadian Sunset', 'Eddie Heywood and Hugo Winterhalter'), ("It's A Sin To Tell A Lie", "Somethin' Smith and The Redheads"), ('The Ballad Of Davy Crockett', 'Tennessee Ernie Ford'), ("I'm Yours", 'Eddie Fisher and Hugo Winterhalter'), ('Skokiaan', 'Ralph Marterie'), ("Theme From 'the Man with the Golden Arm", 'Richard Maltby'), ('Meet Mr. Callaghan', 'Les Paul'), ('Tell Me Why', 'Eddie Fisher and Hugo Winterhalter')]


[ ('Catch A Falling Star / Magic Moments', 'Perry Como'), 




[ ('Superstar', 'Murray Head and The Trinidad Singers'), ('Instant Karma (We All Shine On)', 'John Lennon'), ('Up Around The Bend / Run Through The Jungle', 'Creedence Clearwater Revival'), ("Travelin' Band / Who'll Stop The Rain", 'Creedence Clearwater Revival'), ('Neither One Of Us (Wants To Be The First To Say Goodbye)', 'Gladys Knight and The Pips')]

 []  ('Wake Up Everybody (Pt. 1)', 'Harold Melvin and The Bluenotes'), ('Vincent / Castles In The Air', 'Don Mclean'), ("Breaking Up's Hard To Do", 'Neil Sedaka')]





'''

for i,x in df.iterrows():
    if x['song'] == "I'd Wait A Million Years" and x['artist'] == 'Grass Roots':
        df.at[i, 'text'] = "All of the lonely nights  Waiting for you to come, longing to hold you tight  I need you so desperately  Waiting for you to come bringing your love to me [but]  I'd wait a million years  Walk a million miles, cry a million tears  I'd swim the deepest sea  Climb the highest hill, just to have you near me  As love is reality  When you are near to me, I am in ecstacy  I'd swallow the pain and pride  Baby, I just can't hide all that I feel inside [and]  I'd wait a million years  Walk a million miles, cry a million tears  I'd swim the deepest sea  Climb the highest hill, just to have you near me  A million years, I would wait for you  A million tears, baby I'd be true  A million miles, I would follow you  A million years, if you want me to  Pacing the floor, detest  Sweat pouring down my chest, still I can't love you less  It's worth all the pain and pride  Baby, I just can't hide all that I feel inside [and]  I'd wait a million years  Walk a million miles, cry a million tears  I'd swim the deepest sea  Climb the highest hill, just to have you near me  "

aaaa = df.to_csv("check2.csv")
