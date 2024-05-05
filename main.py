# Making a software that will take input from a user and create an automated speadsheet that contains the rating, average playtime, and any other important information 
# as it pertains to the user
import SteamGames, GeneralGames
steamgames = SteamGames.SteamGames()
generalgames = GeneralGames.GeneralGames()
#game_name = input("What STEAM game would you like to look for? \n")

game = "DaRk SOuLs IIIiY" # Test cases. Input an ID and a title
#game = "374320"

#t = input("Would you like to test if this game is on STEAM? (This may take some time) Y/N \n") # TODO: Make an actual GUI for this, or just make a better input thing
t = "Y"
if t.upper() == "Y": 
    if steamgames.verify_game(game) != None:
        print(f"Search sucessful! {"Steam ID:" if str(steamgames.verify_game(game)).isdigit() else "Game Name:"}\n {steamgames.verify_game(game)}")
        game_name = game if str(steamgames.verify_game(game)).isdigit() else str(steamgames.verify_game(game)).replace("™", "") # Note for future self: Don't forget that 'verify games' outputs the opposite of what you put in (ID/Title)
        game_valid = True
    else:
        print("Game was not found on STEAM...") # TODO: Add an option to retry the search or try for a different game.
        game_valid = False

if game_valid:
    data = (generalgames.getgamedata(game_name))
    for item in data:
        print(f"{item} for {game_name.upper()}: {data[item]}")


