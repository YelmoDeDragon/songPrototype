import requests
from spotify_token_getter import TokenGenerator


class SpotifyAgent:
    def __init__(self):
        self.access_token = None
        self.search_song_url = "https://api.spotify.com/v1/search"
        self.get_access_token()

    def get_access_token(self):
        self.access_token = TokenGenerator().generate_token()

    import requests

    def search_songs(self, query: str):
        params = {
            "q": query,  # texto que escribe el usuario
            "type": "track",  # tipo de búsqueda
            "limit": 6,  # número de resultados
            "market": "MX"  # mercado (opcional)
        }
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(self.search_song_url, headers=headers, params=params)

        # Resultado
        if response.status_code == 200:
            data = response.json()
            tracks = data["tracks"]["items"]

            result = []  # List to hold the song data

            for track in tracks:
                name = track["name"]
                artist = ", ".join([a["name"] for a in track["artists"]])

                # Get the first image (typically the best size for most uses)
                image_url = None
                if track["album"]["images"]:
                    image_url = track["album"]["images"][0]["url"]

                # Append the track information as a dictionary to the result list
                result.append({
                    "name": name,
                    "artist": artist,
                    "image": image_url
                })

            print(result)
            return result  # Return the result as a JSON-like list of dictionaries
        else:
            print("Error:", response.status_code)
            print(response.text)
            return {"error": "Failed to fetch data", "status_code": response.status_code}

my_agent = SpotifyAgent()
my_agent.search_songs("Regalo de dios")
