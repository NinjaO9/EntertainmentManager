# Making a software that will take input from a user and create an automated speadsheet that contains the rating, average playtime, and any other important information 
# as it pertains to the user
import SteamGames
steamgames = SteamGames.SteamGames()
#game_name = input("What STEAM game would you like to look for? \n")

game_name = "Dark SOuls III"

#print(f"Review: {steamgames.get_review(game_name)}")
#print(f"Steam ID: {steamgames.verify_game(game_name)}")
steamgames.checkplatform(3)


