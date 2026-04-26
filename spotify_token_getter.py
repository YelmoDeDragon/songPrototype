import requests
import base64


class TokenGenerator:
    def __init__(self):
        self.access_token = None
        # self.client_id = "a3807595807448ddb469b9e68b12e76f"
        self.client_id = "a153c63639104874a46678279ce9ec46"
        # self.client_secret = "48300a455f23434e94d7c8c03561ec10"
        self.client_secret = "bb154724e58442dd830e05a1f40256d3"
        self.token_url = "https://accounts.spotify.com/api/token"

    def generate_token(self):
        if self.access_token is None:
            credentials = f"{self.client_id}:{self.client_secret}"
            credentials_base64 = base64.b64encode(credentials.encode()).decode()
            headers = {
                "Authorization": f"Basic {credentials_base64}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            data = {
                "grant_type": "client_credentials"
            }
            response = requests.post(self.token_url, headers=headers, data=data)

            if response.status_code == 200:
                token_info = response.json()
                self.access_token = token_info["access_token"]
                print("Access Token:", self.access_token)
                return self.access_token
            else:
                print("Error:", response.status_code)
                print(response.text)
                return None
        else:
            return self.access_token


my_tkn = TokenGenerator()
my_tkn.generate_token()
