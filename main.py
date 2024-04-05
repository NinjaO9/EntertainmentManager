# Making a software that will take input from a user and create an automated speadsheet that contains the rating, average playtime, and any other important information 
# as it pertains to the user
import SteamGames
steamgames = SteamGames.SteamGames()
game_name = input("What STEAM game would you like to look for? \n")


#steamgames.get_review("lies-of-p")
print(f"Game: {game_name}, ID: {steamgames.verify_game(game_name)}")

