import requests, os, typing
from dotenv import load_dotenv
from requests import post

load_dotenv()

class SteamGames():

    applist_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2"

    def _init_(self):
        pass

    @classmethod
    def verify_game(cls, game_name: str) -> int:
        mode = 'appid' if str(game_name).isdigit() else 'name'
        game_list = requests.get(cls.applist_url).json()['applist']['apps']

        for game in game_list:
            if game_name.upper() in str(game[mode]).replace("™", "").upper():
                return (game['appid'] if mode == 'name' else game['name'])
        else:
            print(f"Couldn't find a game with the name '{game_name.upper()}'. Did you type it correctly?")
            return None

    
        






