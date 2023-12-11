from . import get_audio_features as get_audio_features
from . import playlist_comparison as playlist_comparison

def combine_audio_features(top_tracks_url, playlist_audio_features_url):
    cm_top_tracks_audio_features = get_audio_features.get_audio_features(top_tracks_url)

    
    playlist_audio_features = playlist_comparison.playlist_audioFeatures(playlist_audio_features_url)

    combined_audio_features = []

    for x in playlist_audio_features:
        x['crossroads'] = 0
        combined_audio_features.append(x)

    for x in cm_top_tracks_audio_features:
        x['crossroads'] = 1
        combined_audio_features.append(x)

    return combined_audio_features