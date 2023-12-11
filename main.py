import apps.get_audio_features
import apps.playlist_comparison
import apps.combine_top_tracks_playlist as combine_top_tracks_playlist
import pandas as pd

combined_tracks = combine_top_tracks_playlist.combine_audio_features('https://open.spotify.com/artist/5vil8APJ8ohuFhg8mxEOWY?si=JbX0WC5tRhON82I9gIHePA',
                                               'https://open.spotify.com/playlist/37i9dQZF1DWVYgpMbMPJMz?si=40092f47a4874f2b')


print(combined_tracks)