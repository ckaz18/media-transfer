import requests

__SPOTIFY_BASE_URL__ = "https://accounts.spotify.com/api"


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



def make_spotify_request(endpoint, payload):
  response = requests.post(f"{__SPOTIFY_BASE_URL__}{endpoint}", json=payload)
  if response.status_code == 201:  # 201 Created for successful POST
      print("Resource created successfully!")
      return response.json()
  else:
      print(f"Failed to create resource. Status code: {response.status_code}")
      print("Error details:")
      print(response.text)
      return

