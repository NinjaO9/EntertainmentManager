import requests, os, typing
from dotenv import load_dotenv
from requests import post

load_dotenv()

class GeneralGames():
    headers = {
        'Client-ID': os.getenv('clientid'), 
        'Authorization': f'Bearer {os.getenv('access_token')}'
        }
    
    @classmethod
    def getgameid(cls, game_name):
        pass
    
    @staticmethod
    def formatids(platform_ids : str):
        platform_ids = platform_ids.replace("[", "(").replace("]", ")")
        return platform_ids
    
    @classmethod
    def getgameplatforms(cls, platform_ids: str): 
        platform_ids = cls.formatids(platform_ids)
        count = 0
        platforms = post('https://api.igdb.com/v4/platforms', **{'headers': cls.headers,'data': f' fields name; where id = {platform_ids};'}).json()
        for item in platforms: # Separating the id from the name. If I want to include the ID for later purposes, remove/comment out this for loop
            platforms[count] = item['name']
            count += 1
        
        return platforms

    @classmethod
    def getgamedata(cls, game_name) -> None: # Gets game data TODO: Add more data to this, probably. Maybe some cleanup and optimizations later.
        data = {}
        response = post('https://api.igdb.com/v4/games', **{'headers': cls.headers,'data': f'search"{game_name}"; fields *;'}).json()[0]
        data['Rating'] = (str(response['rating'])[:2] + "%")
        data['Platforms'] = cls.getgameplatforms(str(response['platforms']))
        
        return data
