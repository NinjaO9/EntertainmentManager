# Just a file to get a new access token incase mine expires

import requests,os
from dotenv import load_dotenv

load_dotenv()

Client_ID = os.getenv('clientid')
Client_Secret = os.getenv('clientsecret')

print(f"You're new access token information: \n {requests.post(f"https://id.twitch.tv/oauth2/token?client_id={Client_ID}&client_secret={Client_Secret}&grant_type=client_credentials").json()}")