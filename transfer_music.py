from spotify import Spotify
import json

def __main__():
  print("Retrieving users playlists")
  spotify = Spotify()
  spotify.authorize_request()

  playlists = spotify.retrieve_user_playlists()
  print(f"Playlists: {json.dumps(playlists)}")