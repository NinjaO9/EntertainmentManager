# Making a software that will take input from a user and create an automated speadsheet that contains the rating, average playtime, and any other important information 
# as it pertains to the user
import SteamGames, GeneralGames
steamgames = SteamGames.SteamGames()
generalgames = GeneralGames.GeneralGames()
#game = input("What STEAM game would you like to look for? \n")

game = "DaRk SOuLs III" # Test cases. Input an ID and a title
#game = "374320"

game_name = game.upper() # TODO: REMOVE THIS REMOVE THIS REMOVE THIS REMOVE THIS (when ready)
game_valid = True # TODO: THIS TOO THIS TOO THIS TOO THIS TOO
t = "N" #TODO: THIS TOO THIS TOO

#t = input("Would you like to test if this game is on STEAM? (This may take some time) Y/N \n") # TODO: Make an actual GUI for this, or just make a better input thing


if t.upper() == "Y": 
    if steamgames.verify_game(game) != None:
        print(f"Search sucessful! \n{"Steam ID:" if str(steamgames.verify_game(game)).isdigit() else "Game Name:"} {steamgames.verify_game(game)}\n")
        game_name = game.upper() if str(steamgames.verify_game(game)).isdigit() else str(steamgames.verify_game(game)).replace("™", "").upper() # Note for future self: Don't forget that 'verify games' outputs the opposite of what you put in (ID/Title)
        game_valid = True
    else:
        print("Game was not found on STEAM...") # TODO: Add an option to retry the search or try for a different game.
        game_valid = False


if game_valid:
    data = (generalgames.getgamedata(game_name))
    print(f"Data for {game_name}:")
    for item in data:
        print(f"-{item}: {data[item]}")


#generalgames.getgameplatforms(game_name)
#generalgames.getplatforms()
