# Making a software that will take input from a user and create an automated speadsheet that contains the rating, average playtime, and any other important information 
# as it pertains to the user
# import other files
import SteamGames, GeneralGames
#import other libraries
import json, os
steamgames = SteamGames.SteamGames()
generalgames = GeneralGames.GeneralGames()


game = "DarK SoUlS IiI" # Test cases. Input an ID and a title
#game = "374320" # Steam ID (DS3)
#game = "11133" # IGDB ID (DS3)


game_name = game.upper() # TODO: REMOVE THIS REMOVE THIS REMOVE THIS REMOVE THIS (when ready)
t = "N" #TODO: THIS TOO THIS TOO


# TODO: Make an actual GUI for this, or just make a better input thing
class main:
    new_game_list = {}

    @classmethod
    def errorhandler(cls) -> None:
        if input("Would you like to try again? (Y/N) \n").upper() == "Y":
            cls.getdata(game_name=input("What game would you like to search for?\n"))

    @classmethod
    def promptrepeat(cls) -> None:
            if input(f"Would you like to look for another game? (Y/N) \n").upper() == "Y":
                cls.getdata(game_name=input("What game would you like to search for?\n"))
    
    @classmethod
    def getdata(cls, game_name) -> dict:
        if game_name == "":
            print("You didn't type anything in!")
            cls.errorhandler()
        data = (generalgames.getgamedata(game_name))
        if data:
            print(f"Data for search '{game_name}':")
            for item in data: # Debugging stuff, TODO: delete or comment when done
                print(f"-{item}: {data[item]}")
            try:
                if data['Error'] != None:
                    cls.errorhandler()
            except KeyError:
                cls.new_game_list[f"{data['Name']}"] = data
                print(f"Data has been added for the game {data['Name']}!")
                cls.promptrepeat()
        else:
            print(f"An error occured while fetching your game request! Did you type it in correctly?")
            cls.errorhandler()

    @classmethod
    def checklist(cls, game_list: dict) -> dict:
        for game in cls.new_game_list:
            for oldgame in game_list:
                if game == oldgame:
                    print("Duplicate game entry detected! Ignoring..")
            else:
                game_list[f"{game}"] = cls.new_game_list[game]
        return game_list

    @classmethod        
    def setupgamelist(cls) -> None:
        cls.getdata(input("What game would you like to search for? \n"))
        print("Here are the current games in your list:")

        for game in cls.new_game_list:
            print(f"-{game}")
        print("Saving game list...")

        with open("games.json", "a+") as file:
            
            with open("games.json", "r") as f:
                try:
                    game_list = json.load(f)
                    game_list = cls.checklist(game_list)
                except json.decoder.JSONDecodeError as e:
                    print("No current data for 'game_list' found. Creating new instance.")
                    game_list = cls.new_game_list

            with open("games.json", "w") as f: # Probably a baind=aid solution to refreshing the contents of a json in the file, but I'll cross that bridge when I get there.
                file.write(json.dumps(game_list, indent=3))

        print(f"Your game list has been saved to {os.path.join(f"{os.getcwd()}", f"{file.name}")}!")
            

