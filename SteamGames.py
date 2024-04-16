import requests, os, typing
from dotenv import load_dotenv
from requests import post

load_dotenv()

class SteamGames():

    applist_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2"

    def _init_(self):
        pass

    @classmethod
    def verify_game(cls, game_name) -> int:

        if str(game_name).isdigit(): # TODO: If an id is given as an input, verify that the id exists as a game.
            return
    
        applist_params = {"name": game_name}
        game_list = requests.get(cls.applist_url, params=applist_params)
        game_list = game_list.json()
        game_list = game_list['applist']['apps']

        return
        for game in game_list:
            if game_name.upper() in game['name'].replace("™", "").upper():
                app_id = game['appid']
                return (app_id)
        return(f"Couldn't find a game with the name '{game_name.upper()}'. Did you type it correctly?")
    
    @classmethod
    def get_review(cls, game_name) -> str:

        review = post(
        "https://api.igdb.com/v4/games", 
        **{'headers':{"Client-ID":os.getenv('clientid'), "Authorization": f"Bearer {os.getenv('access_token')}"},
        'data':f'search"{game_name}"; fields rating, platforms, release_dates;'})
        cls.checkplatform(str(review.json()[0]))
        return
        return(str(review.json()[0]['rating'])[:2] + "%")
        
    @staticmethod
    def checkplatform(category) -> str:
        #print(overview)
        #console = overview['platforms'][0]
        response = post('https://api.igdb.com/v4/platform_families', **{'headers': {'Client-ID': os.getenv('clientid'), 'Authorization': f'Bearer {os.getenv('access_token')}'},'data': f'search "{category}";fields checksum,name,slug;'})
        print(str(response.json()))
        response = post('https://api.igdb.com/v4/platforms', **{'headers': {'Client-ID': os.getenv('clientid'), 'Authorization': f'Bearer {os.getenv('access_token')}'}, 'data': f'search "{category}";fields *;'})
        with open('test.txt', 'w') as file:
            file.write("response: %s" % str(response.json()))







