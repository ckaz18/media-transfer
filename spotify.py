import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# var authOptions = {
#   url: 'https://accounts.spotify.com/api/token',
#   headers: {
#     'Authorization': 'Basic ' + (new Buffer.from(client_id + ':' + client_secret).toString('base64'))
#   },
#   form: {
#     grant_type: 'client_credentials'
#   },
#   json: true
# };
__SPOTIFY_BASE_URL__ = "https://accounts.spotify.com/api"

class Spotify:
  def __init__(self):
    load_dotenv()
    self.client = os.getenv("SPOTIFY_CLIENT_ID")
    self.secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    self.user = os.getenv("SPOTIFY_USER_ID")
    self.token = ""
    self.expiry = 0 # make this a timestamp value
    
  
  def authorize_request(self,):
    payload = {
       "grant_type": "client_credentials",
       "client_id": self.client,
       "client_secret": self.secret
    }
    response = requests.post(f"{__SPOTIFY_BASE_URL__}/token", data=payload)
    if response.status_code != 201 or response.status_code != 200:
      raise Exception("Unable to validate token")
    else:
      res = response.json()
      self.token = res.get("access_token")
      self.expiry = datetime.now().timestamp()

  def retrieve_user_playlists(self):
    """
    return list of playlist items
    """
    # TODO: implement timestamp validation
    payload  = {
      "grant_type": "playlist-read-private"
    }
    response = requests(f"{__SPOTIFY_BASE_URL__}/users/{self.user}/playlists", data=payload)
    if response.status_code != 200:
      raise Exception("Unable to validate token")
    else:
      res = response.json()
      return res.get("items")
    
