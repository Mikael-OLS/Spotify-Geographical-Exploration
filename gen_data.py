# Load Packages
import spotipy.util as util
import os
from spotipy.oauth2 import SpotifyClientCredentials
import pickle as pk
import pandas as pd
import geopandas as gpd

# Set your Spotify API passwords 
cid = 'cid'
secret = 'secret'
username = 'username'
urir = 'urir'


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 


# Get read access to your library
scope = 'playlist-modify-private user-read-recently-played playlist-read-private user-follow-read user-read-currently-playing playlist-modify-public user-library-read user-follow-modify user-read-private user-library-modify user-read-playback-state user-read-playback-position user-top-read streaming user-modify-playback-state'

token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri=urir)
sp = spotipy.Spotify(auth = token)

# Read country geagraphical file
shapefile = '/Users/mikael/Desktop/Spyder/TowardsDataScience/spotify/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'

gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

# Rename columns
gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()
gdf = gdf.drop(gdf.index[159])

# Make translate dict 
translate_l = {
     'Argentina': 'Argentina',
     'Australien': 'Australia',
     'Österrike': 'Austria',
     'Belgien': 'Belgium',
     'Brasilien': 'Brazil',
     'Bulgarien': 'Bulgaria',
     'Chile': 'Chile',
     'Colombia': 'Colombia',
     'Costa Rica': 'Costa Rica',
     'Tjeckien': 'Czechia',
     'Danmark': 'Denmark',
     'Dominikanska republiken': 'Dominican Republic',
     'Ecuador': 'Ecuador',
     'El Salvador': 'El Salvador',
     'Estland': 'Estonia',
     'Finland': 'Finland',
     'Frankrike': 'France',
     'Tyskland': 'Germany',
     'Grekland': 'Greece',
     'Guatemala': 'Guatemala',
     'Honduras': 'Honduras',
     'Hongkong': 'China',
     'Ungern': 'Hungary',
     'Island': 'Iceland',
     'Indien': 'India',
     'Indonesien': 'Indonesia',
     'Irland': 'Ireland',
     'Israel': 'Israel',
     'Italien': 'Italy',
     'Japan': 'Japan',
     'Lettland': 'Latvia',
     'Litauen': 'Lithuania',
     'Luxemburg': 'Luxembourg',
     'Malaysia': 'Malasyia',
     'Malta': 'Malta',
     'Mexiko': 'Mexico',
     'Nederländerna': 'Netherlands',
     'Nya Zeeland': 'New Zeeland',
     'Nicaragua': 'Nicaragua',
     'Norge': 'Norway',
     'Panama': 'Panama',
     'Paraguay': 'Paraguay',
     'Peru': 'Peru',
     'Filippinerna': 'Philippines',
     'Polen': 'Poland',
     'Portugal': 'Portugal',
     'Rumänien': 'Romania',
     'Singapore': 'Singapore',
     'Slovakien': 'Slovakia',
     'Sydafrika': 'South Africa',
     'Spanien': 'Spain',
     'Sverige': 'Sweden',
     'Schweiz': 'Switzerland',
     'Thailand': 'Thailand',
     'Turkiet': 'Turkey',
     'Storbritannien': 'United Kingdom',
     'USA': 'United States of America',
     'Uruguay': 'Uruguay',
     'Vietnam': 'Vietnam',
     'Taiwan':'Taiwan',
     'Canada':'Canada',
     'Russ':'Russia'
    }

# Read Country name file 
land = pd.read_csv('data.csv')

# Add some other list 
andra = ['Topp 50 i Taiwan','Topp 50 russ','Topp 50 canada']

# Make a df with the toplists
plid = {}
for i in land.Name:
    stringo = 'topp i ' + i
    print(stringo)
    ser = sp.search(stringo, type='playlist', limit = 1)
    if ser['playlists']['items']:
        plid[(ser['playlists']['items'][0]['name'])] = sp.playlist_tracks(ser['playlists']['items'][0]['uri'], limit = 50)

for i in andra:
   ser = sp.search(i, type='playlist', limit = 1)
   if ser['playlists']['items']:
       plid[(ser['playlists']['items'][0]['name'])] = sp.playlist_tracks(ser['playlists']['items'][0]['uri'], limit = 50)


delcol = ['#TopPolyfAv Reggae_DJKaVa_Buka_Sokovagone','AFRI-CAN! ','Cameroun Top Gospel 2020','Hot Hits Canada','Kazakhstan Chart Toppers 2017-2018. Воспоминания о Казахстане.','Top New Reggae','Serbian Ukranian Bosnian Russian Algerian Israeli American Malian Grooves and Grooviness' ]
for i in delcol:
    del plid[i]


# Make df with the top tracks
toptracks = []
for j,i in  enumerate(plid):
    pl = plid[i]['items']
    for k in range(0,len(pl)):
        toptracks.append(pl[k]['track']['name'])

# Make df with the top genres
topgenres = []
for j,i in  enumerate(plid):
    pl = plid[i]['items']
    for k in range(0,len(pl)):
        artist_id = pl[k]['track']['artists'][0]['id']
        artist = sp.artist(artist_id)
        genres = artist['genres']
        print(genres)
        topgenres.append(genres)

for i in range(0,len(topgenres)):
    if len(topgenres[i]) > 0:
        topgenres[i] = topgenres[i][0]
    else topgenres.pop(topgenres)


# Make a df with the countries and their varieblaes(POP,HIPHOP,LATIN,DANCE,ENERGY,ACOUST)
def country_df(dicc, translate):
    rer = pd.DataFrame()
    landlist = []
    poplist = []
    raplist = []
    latinlist = []
    dancelist = []
    energylist = []
    acoustlist = []
    for j,i in  enumerate(dicc):
        if 'Topp 50 i' in i:
            land = str(i[10:])
        elif 'Top 50' in i:
            land = str(i[7:])
        elif 'Topp 50 Russ' in i:
            land = str(i[8:])
        land = translate[land]
        pl = dicc[i]['items']
        pop = 0
        rap = 0
        latin = 0
        dance = 0
        energy = 0
        acoust = 0
        count = 0
        for k in range(0,len(pl)):

            artist_id = pl[k]['track']['artists'][0]['id']
            artist = sp.artist(artist_id)
            genres = artist['genres']
            for d in genres:
                count = count + 1
                if 'pop' in d:
                    pop = pop + 1
                if 'rap' in d:
                    rap = rap + 1
                elif 'hip hop' in d:
                    rap = rap + 1
                if 'latin' in d:
                    latin = latin + 1
                    
            song_id = pl[k]['track']['id']
            song = sp.audio_features(song_id)
            dance =  dance + song[0]['danceability']
            energy = energy + song[0]['energy']
            acoust = acoust + song[0]['acousticness']
        pop = pop/count
        rap = rap/count
        latin = latin/count
        dance = dance/len(pl)
        energy = energy/len(pl)
        acoust = acoust/len(pl)
        
        landlist.append(land)
        poplist.append(pop)
        raplist.append(rap)
        latinlist.append(latin)
        dancelist.append(dance)
        energylist.append(energy)
        acoustlist.append(acoust)

    rer['Country'] = landlist
    rer['Pop %'] = poplist
    rer['Hip Hop %'] = raplist
    rer['Latin %'] = latinlist
    rer['Energy'] = energylist
    rer['Danceability'] = dancelist
    rer['Acousticness'] = acoustlist
    return(rer)


country_data = country_df(plid, translate_l)

# Save data
pk.dump( country_data, open( "country_data.p", "wb" ) )
pk.dump( toptracks, open( "toptracks.p", "wb" ) )
pk.dump( topgenres, open( "topgenres.p", "wb" ) )
