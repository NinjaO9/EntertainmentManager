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


# TODO: Make an actual GUI for this, or just make a better input thing 1012
class main:
    game_list = {}

    @classmethod
    def errorhandler(cls) -> None:
        if input("Would you like to try again? (Y/N) \n").upper() == "Y":
            cls.getdata(game_name=input("What game would you like to search for?\n"))

    @classmethod
    def promptrepeat(cls) -> None:
            if input(f"Would you like to look for another game? (Y/N) \n").upper() == "Y":
                cls.getdata(game_name=input("What game would you like to search for?\n"))
    
    @classmethod
    def getdata(cls, game_name) -> dict: # gotta return the dict eventually
        if game_name == "":
            print("You didn't type anything in!")
            cls.errorhandler()
        data = (generalgames.getgamedata(game_name))
        if data:
            print(f"Data for search '{game_name}':")
            for item in data: # Debugging stuff, delete or comment when done
                print(f"-{item}: {data[item]}")
            try:
                if data['Error'] != None:
                    cls.errorhandler()
            except KeyError:
                cls.game_list[f"{data['Name']}"] = data
                print(f"Data has been added for the game {data['Name']}!")
                cls.promptrepeat()
        else:
            print(f"An error occured while fetching your game request! Did you type it in correctly?")
            cls.errorhandler()

    @classmethod        
    def setupgamelist(cls):

        cls.getdata(input("What game would you like to search for? \n"))
        print("Here are the current games in your list:")
        for game in cls.game_list:
            print(f"-{game}")
        print("Saving game list...")
        with open("games.json", "a") as file:
            file.write(json.dumps(cls.game_list, indent=3))
        print(f"Games have been saved to {os.path.join(os.getcwd(), file)}")
            



    #getdata(game_name)
    '''
    def metaverse() -> None: # Find a better name
        if input("Would you like to find data for another game? (Y/N)") == "Y":
            ebola(input("What STEAM game would you like to look for? \n"))

    def checksteamvalidity(game) -> str:
        if steamgames.verify_game(game) != None:
            print(f"Search sucessful! \n{"Steam ID:" if str(steamgames.verify_game(game)).isdigit() else "Game Name:"} {steamgames.verify_game(game)}\n")
            game_name = game.upper() if str(steamgames.verify_game(game)).isdigit() else str(steamgames.verify_game(game)).replace("™", "").upper() # Note for future self: Don't forget that 'verify games' outputs the opposite of what you put in (ID/Title)
            return game_name
        else:
            print("Game was not found on STEAM...") # TODO: Add an option to retry the search or try for a different game.
            return None

    def ebola(game) -> None: # Find a better name
        if input("Would you like to test if this game is on STEAM? (This may take some time) Y/N \n") == "Y":
            game_name = checksteamvalidity(game)
        game_name = game
        getdata(game_name)
        metaverse()
    '''

main.setupgamelist()
