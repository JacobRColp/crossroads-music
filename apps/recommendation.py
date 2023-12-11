import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.environ.get('client_secret')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_link = 'https://open.spotify.com/artist/5vil8APJ8ohuFhg8mxEOWY?si=JbX0WC5tRhON82I9gIHePA'
artist_uri = artist_link.split("/")[-1].split("?")[0]

#print(sp.recommendation_genre_seeds())

recommendations = sp.recommendations(seed_artists=[artist_uri],
                    seed_genres=['gospel', 'acoustic'],
                    seed_tracks=['spotify:track:2lG2pPRdk26Yz2gD6bQoUF'],
                    country='US',
                    limit=1)

print(recommendations)

#TODO: Pass recommendations into audio feature endpoint
#TODO: Comparison of CM songs to recommendations audio features

pass