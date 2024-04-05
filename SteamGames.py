import requests
from bs4 import BeautifulSoup
from universal import *

class SteamGames():

    applist_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2"

    def _init_(self):
        pass

    def verify_game(self, game_name) -> str:

        if str(game_name).isdigit():
            return
    
        applist_params = {"name": game_name}
        game_list = requests.get(self.applist_url, params=applist_params)
        game_list = game_list.json()
        game_list = game_list['applist']['apps']

        for game in game_list:
            if game_name in game['name']:
                self.app_id = game['appid']
                return self.app_id
        else:
            return(f"Couldn't find a game with the name '{game_name}'. Did you type it correctly?")
    
    def get_review(self, game_name) -> float: # Not ready AT ALL

        #review = requests.get(f"{reviewlink}game/{game_name}")
        #review = requests.get('https://howlongtobeat.com/game/2225')
        #review = BeautifulSoup(review.content, 'html.parser')

        #print(review)
        return
        # Going through the jungle...

        #review = review('div', class_='c-layoutDefault_page')

        review = review.select_one('c-siteReviewScore u-flexbox-column u-flexbox-alignCenter u-flexbox-justifyCenter g-text-bold c-siteReviewScore_green g-color-gray90 c-siteReviewScore_medium')
        review = review.text.strip()
        print(review)




