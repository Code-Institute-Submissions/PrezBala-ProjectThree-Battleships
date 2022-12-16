# Battleships - Project 3

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/maincover.png">

This project is based on the Battleship game which is a game that is very widely know. This game is Python based game which runs within the Code Institite mock terminal within Heroku. The main purp[ose of the game is for the user to play against the computer and the user will have 10 turns to find all of their opponents ships before there ship gets destroyed. 

[Live link to the game](https://prasena-project-3-battleships.herokuapp.com/)

<hr>

# Table of Contents
<!-- TOC start -->

- [User Experience)](#ux-user-experience)
  * [Game Goal](#Battle-Ship-game-goals)
- [How the game works](#How-the-game-works)
- [Game basics and features](#game-basics-and-features)
- [Input Validation](#Input-Validation)
- [Data Model](#Data-Model)
- [Libraries](#Libraries)
- [PEP8 pip3 validator](#PEP8-pip3-validator)
- [Deployment](#Deployment)
- [Credits and Acknowledgements](#Credit-and-Acknowledgements)
- [Future Features](#Future-Features)
  
<!-- TOC end -->
<!-- TOC -->

<hr>

# UX (User Experience)
## Battle Ship game goals

The main purpose for this game is to engage the user in a fun battleships game against the computer. By being able to enter your name you can engage against the computer and be able to see your board clearly. The boards are randomly generated for every game that is played and actively updating showing where the guesses were made on the board. If the player hit one of the computers ships it will be marked "X" but if the player misses then "-" will be displayed. I've allowed 10 turns for the player to try and guess where all the ships for the computers are placed, otherwise it will be game over! 

<hr>

# How the game works

Python based game where the user can challenge the computer in a match of Battleships.

<ol>
<li>When the game is loaded it will prompt the user with a greeting and ask for a user name with the ASCII art of a ship displaying above </li>
<li>Once the user has entered there name the game will begin displaying both the user board and the computer board. On the users board the ships will be marked as '@'</li>
<li>Players will have 12 guesses to hit the computers 8 ships, winner at the end of all the turns is the one with the most hit ships, if the player or computer hit all 8 ships first then they will be the winner.</li>
<li>The user will be prompted with a message "Please enter a ship row 1-8" and once entered they will be prompted with "Please enter a ship column A-H"</li>
<li>The computer will also take a guess and once made the user will be notified in the message stating if the user has hit or miss and also what cell the computer has made</li>
<li>The user will then be notified if they wish to continue playing with the options of "y/n" If the user select "y" the game will continue and the locations of where the guess for the ships that was made in the previous turn will now be updated on the board. If the user selected "n" then  a game over message will appear and conclude the game</li>
players board if the computer hit a ship on the players board.</li>
<li>The boards will be updated once the game is continued from the previous turns, if the user or computer hit a target it will be marked with "X" but if missed then a "-" symbol will appear on the board </li>
<li>The user will continue across all 12 turns and the process will repeat until either the user or the computer hit the most ships/all the ships first. The winner will be decided on who hit the most ships </li>
<li>Once all turns are complete the game will announce the winner within the message notification</li>
</ol>

<hr>

# Game basics and features

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/gamestart1.png">

+ When starting up the game the user will be presented with ASCII art and text showing a battleship with the title above. The user will be advised they have 12 turns and to 
also input there name to continue.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/hiddenboard.png">

+ I've also added a hiddenboard for testing purposes, this shows the location of where all the ships are for the computer. I've used this board to test different functionalities when either hitting or missing there ship. This will be hidden prior submission as the player should not know the answers once the game is released!

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/gamestart2.png">

+ Once the user name is entered the user will be presented with both their board and the computers board. The user will have full visibility of the location of their ships while
the opponents will be hidden until struck/missed in a turn.

+ Throughout the game it will maintain the same terminal appearence, showing both boards and updating accordingly whether the ship on either side per turn was hit or not. If hit a "X" will be marked and if missed "-" will be there instead.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/gamestart3.png">

+ The above board the user has entered 2A as a guess, which unfortunetly was a miss. The computer has also missed by guessing value 5G, the user will be notified
how many turns they have remaining and also the total scores for both the user and the computer. The user will be requested if they wish to continue playing at the end of the turn.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/gamestart4.png">

+ The missed location will also be updated on the board once the user confirms to continue playing. A "-" symbol will appear on both the user and the computers board to indicate where the previous guess was made.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/stopplaying.png">

+ If the user decides at any point during the end of their turn that they wish to conclude playing they can type "n" for when asked if they wish to continue playing. Doing so will conclude the game.

<hr>

# Input Validation

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/bareexceptfix.png">

+ User is advised to enter correct value within the parameters requested. User is notified with text "Sorry, number between 1 - 8 required, please try again"  and also
letter between A-H required, you provided '5'" 

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/alreadyguessed.png">

+ When the user re-enters the same values they've used before in a prvious turn they will be notified of this and this will not use up a turn. The user is given an option to continue playing and choose a different value or end the game.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/gamewon.png">

+ In the event that a user guesses the location of all 8 of the computers battleships, a message will appear and the game will conclude.
I've increased the count of ships to 8 and also increased the turns to 12 from when i first created the functions for a higher chance for the user to win.

<hr>

# Data Model

I've created 3 boards when initially setting up this game. A hidden board which will be used for testing purposes, this board shows the user all the locations of the computers ships so this will help figure out any bugs and also if my functions are working correctly when hitting / missing their ship. Guess board for the user to make their guesses on the computers ships and also the User board with the location of their own battleships. Initially i had a lower turn and ship count but found after testing myself it was quite difficult to win, so i've increased the total turn count to 12 and ships to 8.

I've created the board with the dimensions Columns A-H and row 1-8. Each turn both the user and computer take guesses on the location of the other players ships, when a successful hit is made by either user or computer this will be marked on the board as 'X' the function def count_hit_ships(board) will ensure the score will increase by 1 . Once a turn is over the boards will be updated showing either a 'X' or '-' for both ships hit and those missed.  

After every turn the board will update and eventually the game will conclude and both function if count_hit_ships(GUESS_BOARD) == 8:  and if count_hit_ships(USER_BOARD) == 8: will work to advise which player has won (if they managed to find all the battleships!)

<hr>

# Libraries

+ Colorama library was used to generate the colours for the code. [here](https://pypi.org/project/colorama/)

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/import.png">

I've decided to use the above library as it was easier and also clearer for the project assessor to see the colour references for example the below image
shows the prRed using the Colorama library whereas the prGreen was using my previous method which isn't very clear with what exactly the function is doing.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/colorama.png">

<hr>

# PEP8 pip3 validator

Due to pep8online.com being down as advised by my mentor i've used PEP8 validator within Gitpod Workspace, the steps i'vetaken are below.

+ running the command pip3 install pycodestyle
+ Run the command pip3 install pycodestyle
+ press Ctrl+Shift+P 
+ Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results
+ Select pycodestyle from the list 
+ PEP8 errors appeared underlined in red, as well as being listed in the PROBLEMS tab.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/error4.png">

Error "expected 2 blank lines found 1" i've added additional lines between the colours (def prRed and def prGreen for example) to ensure there is now 2 blank lines.
Once this change has been made the errors have cleared for that specific comment.

Error "do not use bare except" after googling and reading online i found the way to correct this is by adding additional text after the except value, so i've added ValueError after the except function and after testing the game this has resolved that issue and cleared the error.

Error "over-indented" this was due to the aligning of my functions, specifically the prGreen/Purple/Yellow etc. I've tidied the code up and ensure they are placed in the correct manner and tested out the functions once changes made. This has cleared the error once indented correctly.

I've encountered the below error when first running the game with the python3 run.py command, these were quickly corrected as i found the error to be on the 
ASCII art battleship, some of the '/' used were recognised as a function instead of it being just an aesthetic reason, so i've personally made changes on the ship to ensure
this is corrected and ran the game again using the run.py to check that both the game works ok and the ship appears correctly.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/error2.png">

I've also used the Code Institute CI Python Linter validator which came through with no errors.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/linter.png">

An error regarding invalid escape sequence with my Battleship ASCII art. I've googled and carried out a few tests and found by adding a 'r' before the '"'  to prCyan(r""") this resolved all errors. This was tested again in Heroku to ensure issue is resolved.

<img src="https://github.com/PrezBala/ProjectThree-Battleships/blob/main/assets/images/error8.png">

I've also encountered an issue with the "pip install colorama" function as i found that everytime i started a new workspace it did not retain the library that was installed.
Though after speaking to Student support i found that this was due to me using new workspaces with every session! so by clearing up my workspaces and placing a 'pin' on my current session i then found the issue to be resolved. 



<hr>

# Deployment

+ This project was deployed using Code Institute's mock terminal for Heroku.
+ Go to the Heroku app and create and account
+ You will need to add PORT 8000 to Config Vars in the Settings tab
+ Set the buildbacks to Python and NodeJS in that order
+ In the Deployment tab select GitHub as the Deployment method
+ Link the Heroku app to the repository
+ You can choose either automatic or manual deploy and select 'Deploy Branch'

<hr>

# Credits and Acknowledgments

+ My mentor Andre Aquilina who guided me in troubleshooting certain errors and providing links to certain articles that aided me in this project.
+ YouTube, codeacademy and knowledge mavens youtube channel to inspire with ideas and how to handle errors and validation, and for generating the board that was used for this game. I watched Mavens video several times and made notes as I was going along to break down each step and make the game my own by adding an additional board for the computer.
+ Python for beginners reddit page that provided several answers to any questions i had and also helped me as i can easily search through any similar queries other people had compared to mine.
+ Code institute for allowing me to use the template and being able to deploy it on the Heroku App.
+ Tutor Support in Code Institute for pointing our my workspace issue and the pip install function.
+ The battleships text in ascii was created using an ascii generator found [here](https://patorjk.com/software/taag/#p=display&f=Doom&t=Battleships)
+ The battleship image in ascii was taken from [here](https://www.asciiart.eu/vehicles/navy)

<hr>

# Future Features

+ Allow the user to make changes to the board size, total number of ships and even place the ships at a location they would like.
+ Increase the size of the ship instead of it being 1x1
+ By adding bigger ships perhaps have a bigger score for hitting that.
+ Improve naming my functions and variables but will improve this in time by practicing by creating other games in my own time within Python.


[Back to Table of Contents](https://github.com/PrezBala/ProjectThree-Battleships#table-of-contents) 