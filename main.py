# Making a software that will take input from a user and create an automated speadsheet that contains the rating, average playtime, and any other important information 
# as it pertains to the user
import SteamGames, GeneralGames
steamgames = SteamGames.SteamGames()
generalgames = GeneralGames.GeneralGames()

game = "DarK SoUlS IiI" # Test cases. Input an ID and a title
#game = "374320" # Steam ID (DS3)
#game = "11133" # IGDB ID (DS3)


game_name = game.upper() # TODO: REMOVE THIS REMOVE THIS REMOVE THIS REMOVE THIS (when ready)
t = "N" #TODO: THIS TOO THIS TOO


# TODO: Make an actual GUI for this, or just make a better input thing 1012

def errorhandler():
    if input("Would you like to try again? (Y/N) \n").upper() == "Y":
        getdata(game_name=input("What game would you like to search for?\n"))

def getdata(game_name) -> dict: # gotta return the dict eventually
    data = (generalgames.getgamedata(game_name))
    if data:
        print(f"Data for search '{game_name}':")
        for item in data:
            print(f"-{item}: {data[item]}")
        try:
            if data['Error'] != None:
                errorhandler()
        except KeyError:
            pass
    else:
        print(f"An error occured while fetching your game request! Did you type it in correctly?")
        errorhandler()
        

getdata(game_name)
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


ebola(input("What STEAM game would you like to look for? \n"))
'''