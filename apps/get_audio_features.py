import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.environ.get('client_secret')

#crossroads artist link = 'https://open.spotify.com/artist/5vil8APJ8ohuFhg8mxEOWY?si=JbX0WC5tRhON82I9gIHePA'

def get_audio_features(artist_link):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    link = artist_link
    artist_uri = link.split("/")[-1].split("?")[0]

    cm_topTracks = sp.artist_top_tracks(artist_uri)

    topTrack_URI = [x['uri'] for x in cm_topTracks['tracks'] ]

    cm_audioFeatures = [x for x in sp.audio_features(topTrack_URI)]

    name_Uri = {}

    for x in cm_topTracks['tracks']:
        name_Uri[x['name']]=x['uri']


    for x in name_Uri:
        for y in cm_audioFeatures:
            if name_Uri[x] == y['uri']:
                y['song_name'] = x
            else:
                continue

    cm_topTracks_popularity_holding = {}

    for x in cm_topTracks['tracks']:
        cm_topTracks_popularity_holding[x['uri']] = x['popularity']

        for x in cm_topTracks_popularity_holding:
            for y in cm_audioFeatures:
                if x == y['uri']:
                    y['popularity'] = cm_topTracks_popularity_holding[x]
                else:
                    continue

    return cm_audioFeatures



