import requests
from bs4 import BeautifulSoup
from universal import *
from temp import *

class SteamGames():

    applist_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2"

    def _init_(self):
        pass

    def verify_game(self, game_name) -> str:

        if str(game_name).isdigit(): # TODO: If an id is given as an input, verify that the id exists as a game.
            return
    
        applist_params = {"name": game_name}
        game_list = requests.get(self.applist_url, params=applist_params)
        game_list = game_list.json()
        game_list = game_list['applist']['apps']

        for game in game_list:
            if game_name.upper() in game['name'].upper():
                self.app_id = game['appid']
                return (f"App ID: {self.app_id}")
        else:
            return(f"Couldn't find a game with the name '{game_name.upper()}'. Did you type it correctly?")
    
    def get_review(self, game_name) -> float: # Not ready AT ALL

        review = requests.post("https://api.igdb.com/v4/games", 
                                **{'headers':{"Client-ID":clientid, "Authorization": f"Bearer {access_token}"},
                                   'data':f'search"{game_name}"; fields rating;'})
        return(f"Rating: {str(review.json()[0]['rating'])}")
        




