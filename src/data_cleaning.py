import json
import pandas as pd

def main():
  flat_data = {
    'playlist_id': [],
    'playlist_name': [],
    'track_uri': [],
    'track_name': [],
    'artist_name': [],
    'album_name': []
  }
  files = [
    '../data/spotify1.json',
    '../data/spotify2.json',
    '../data/spotify3.json',
    '../data/spotify4.json'
  ]

  for file_path in files:
    with open(file_path) as json_file:  
      data = json.load(json_file)
      for playlist_index, playlist in enumerate(data['playlists'], start = 1):
          for track in playlist['tracks']:
            flat_data['playlist_id'].append(file_path + '-' + str(playlist_index))
            flat_data['playlist_name'].append(playlist['name'])
            flat_data['track_uri'].append(track['track_uri'])
            flat_data['track_name'].append(track['track_name'])
            flat_data['artist_name'].append(track['artist_name'])
            flat_data['album_name'].append(track['album_name'])  

  songs_df = pd.DataFrame.from_dict(flat_data)
  songs_df.to_csv(r'../data/spotify_clean.csv')

if __name__== "__main__":
  main()