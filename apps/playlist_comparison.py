import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.environ.get('client_secret')

#WorshipNOW playlist = 'https://open.spotify.com/playlist/37i9dQZF1DWVYgpMbMPJMz?si=40092f47a4874f2b'

def playlist_audioFeatures(playlist_url):

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    url = playlist_url
    playlist_uri = url.split("/")[-1].split("?")[0]

    playlist_tracks = sp.playlist_items(playlist_uri)

    uri_dict = {}

    for x in playlist_tracks['items']:
        uri_dict[x['track']['name']] = x['track']['uri']

    list_audioFeatures = sp.audio_features(uri_dict.values())

    for x in list_audioFeatures:
        for y in uri_dict:
            if x['uri'] == uri_dict[y]:
                x['song_name'] = y
            else:
                continue

    popularity_holding = {}

    for x in playlist_tracks['items']:
        popularity_holding[x['track']['uri']] = x['track']['popularity']

    for x in list_audioFeatures:
        for y in popularity_holding:
            if x['uri'] == y:
                x['popularity'] = popularity_holding[y]
            else:
                continue

    return list_audioFeatures


