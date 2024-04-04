from os import getenv

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()


client_id = getenv("CLIENT_ID")
client_secret = getenv("CLIENT_SECRET")


client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get the playlist

playlist_url = (
    "https://open.spotify.com/playlist/1ouStNfRjagW9NpFk95IrR?si=eLucbKsqTFyVz8EanZ065g"
)

playlist_id = playlist_url.split("/")[-1].split("?")[0]

playlist: dict = sp.playlist_tracks(playlist_id)  # type: ignore

print(playlist.keys())
for idx, track in enumerate(playlist["items"]):
    print(f"{idx+1:2}. {track['track']['name']}")
