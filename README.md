This is a project I had in mind that was meant to allow for a little library of entertainment(Games, movies, shows) for the user. 
Essentially, it was meant to be a clean way to have a collection of entertainment to help with things like backlogs and other lists of the sort. 

**How do I use it?**
You will have to follwo the account creation steps shown here: https://api-docs.igdb.com/#getting-started
Then, once you get your Client ID and Access token, set an .env file to contain the values of 'client-id', and 'access_token' to their appropriate values.
Ensure that you have the proper libraries installed.
Afterwards, you should be able to run the program without issues


**How does it work?**
  Currently, the program uses the IGDB API to get information about games. (https://www.igdb.com). Through the API, the program searches through an endpoint with the name of the closest game that the user types to search.
  Through the endpoint, the program will get specific details about the game through the use of other endpoints (if available), and neatly list them off to the user before requesting another game (if the user decides to input another game.)
  After a list of games is created (a list of the current instance of games search in succession,) the program will create a .txt file (if one doesn't exist for the program already,) and place a converted pyhton dictionary (JSON file)
  inside with the information of each game searched. If another search inquiry is done afterwards, then the JSON is converted back into a pyhton dictionary, where duplicate entries are removed and new entries are added to the old list,
  and converted back into a JSON.
  
As of the writing of this README, the method of finding games and their statistics has (mostly?) been completed. 
  There are no inplementations of movie and show statistics inside the program at this time.

With the most recent commit:
  I tried to mess around with some GUI stuff. I think I might hold that off for later on, after I get implementation with movies and shows.

Here is a list of stuff I would like to add if I continue working on this project:
- Show database (Need to find an API)
- Movie database (^)
- Steam compatability*
- GUI (Need to study GUIs more)
- Easy way to get a custom token for the program to run (This one seems a bit farfetched)
are 
* Steam compatibility would be me asking the user for their steam ID, and then searching through their account for games that IGDB contains, or even if I can get ahold of steam game info, and appllying it to the same principles that the IGDB games are following.
