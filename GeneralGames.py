import requests, os, typing
from dotenv import load_dotenv
from requests import post

load_dotenv()

class GeneralGames():
    headers = {
        'Client-ID': os.getenv('clientid'), 
        'Authorization': f'Bearer {os.getenv('access_token')}'
        }
      
    def __init__(self) -> None:
        pass
    
    @classmethod
    def getgameid(cls, game_name):
        pass
    

    @classmethod
    def getgamedata(cls, game_name) -> None: # Gets game data TODO: Add more data to this. Maybe make more, mini functions that are called just to make this function cleaner
        data = {}
        response = post('https://api.igdb.com/v4/games', **{'headers': cls.headers,'data': f'search"{game_name}"; fields *;'})
        data['Review'] = (str(response.json()[0]['rating'])[:2] + "%")
        return data
        '''with open('oldtest.txt', 'w') as file:
            file.write(f"platforms ids: {str(platform_ids)}")'''

    @classmethod
    def getgameplatforms(cls, game_name): # Possible temp function. I dunno if I will merge it with getgamedata
        response = post('https://api.igdb.com/v4/games', **{'headers': cls.headers,'data': f'search"{game_name}"; fields platforms;'})
        platform_ids = response.json()[0]['platforms']
        with open('oldtest.txt', 'w') as file:
            file.write(f"platforms ids: {str(platform_ids)}")

    @classmethod # Trying to see the ids of different platforms
    def getplatforms(cls): # Not all platforms are showing up? I think?
        limit = 100 
        offset = 0
        console_ids = []
        while True:
            
            # I asked chatgpt for help, still can't get anymore than the same 10 results ._.
            response = post('https://api.igdb.com/v4/platforms', **{'headers':cls.headers, 'data': f';fields id; limit {limit}; offset {offset}'})
            platforms = response.json()
            if not platforms:
                break  # No more results, exit the loop
            console_ids.extend(platform["id"] for platform in platforms)
            offset += limit  # Move to the next page
            with open('oldtest.txt', 'w') as file:
                file.write(f"response: {str(console_ids)}")
                print(f"Completed!, offset: {offset}, limit: {limit}")