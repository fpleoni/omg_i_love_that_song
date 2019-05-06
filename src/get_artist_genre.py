import json
import pandas as pd

def main():
  flat_data = {
    'playlist_id': [],      
    'artist_uri': [],
    'album_uri': []
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
            flat_data['artist_uri'].append(track['artist_uri'])
            flat_data['album_uri'].append(track['album_uri'])  

  songs_df = pd.DataFrame.from_dict(flat_data)
  songs_df.to_csv(r'../data/artist_album_ids.csv')

if __name__== "__main__":
  main()