import requests, os, typing
from dotenv import load_dotenv
from requests import post

load_dotenv()

class GeneralGames():
    headers = {
        'Client-ID': os.getenv('clientid'), 
        'Authorization': f'Bearer {os.getenv('access_token')}'
        }
    
    @staticmethod
    def formatids(ids : str) -> list:
        ids = ids.replace("[", "(").replace("]", ")")
        return ids
    
    @classmethod
    def getgameplatforms(cls, platform_ids: str) -> list: 
        platform_ids = cls.formatids(platform_ids)
        count = 0
        platforms = post('https://api.igdb.com/v4/platforms', **{'headers': cls.headers,'data': 'fields name;' f'where id = {platform_ids};'}).json()
        for item in platforms: # Separating the id from the name. If I want to include the ID for later purposes, remove/comment out this for loop
            platforms[count] = (item['name'])
            count += 1
        return platforms
    
    @classmethod
    def getgamegenres(cls, genre_ids: str) -> list:
        genre_ids = cls.formatids(genre_ids)
        count = 0
        genres = post('https://api.igdb.com/v4/genres', **{'headers': cls.headers,'data': 'fields name;' f'where id = {genre_ids};'}).json()
        for genre in genres:
            genres[count] = (genre['name'])
            count += 1
        return genres

    
    @classmethod
    def getcover(cls, coverID) -> str:
        cover_link = str(post('https://api.igdb.com/v4/covers', **{'headers': cls.headers, 'data': f'fields url;' f'where id = {coverID};'}).json()[0]['url']) #this will return a small image of the cover. Come back and modify to return a normal size later.
        return 'https:' + cover_link.replace('thumb', 'cover_big')

    @classmethod
    def getgamedata(cls, game_name) -> dict: # Gets game data TODO: Add more data to this, probably. Maybe some cleanup and optimizations later.
        data = {}

        try:
            rawdata = post('https://api.igdb.com/v4/games', **{'headers': cls.headers,'data': f'search"{game_name}";' 'fields *;'}).json()[0]
        except IndexError:
            return None
        try:
            data['Name'] = str(rawdata['name']) 
            data['Rating'] = (str(rawdata['rating'])[:2] + "%")
            data['Platforms'] = cls.getgameplatforms(str(rawdata['platforms']))
            try: # data['has DLC']
                data['Has DLC'] = "Yes" if (rawdata['expansions'] != '[]') else "No"
            except KeyError:
                data['Has DLC'] = "No"
            data['Cover'] = cls.getcover(str(rawdata['cover']))
            data['Genre'] = cls.getgamegenres(str(rawdata['genres']))
            #data['Developer(s)']
        except KeyError:
            data['Error'] = "An error occured while fetching some data!\n   It is likely that there is not enough information about this game."
        
        return data
