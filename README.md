# Project Portfolio 3 - Python

## One-Armed Bandit!

> known also as slot machine (American English), fruit machine (British English) or poker machine (Australian English and New Zealand English and is a gambling game that creates a game of chance for its customers [Wikipedia](https://en.wikipedia.org/wiki/One_Armed_Bandit) 

It is a Python terminal game, deployed on Heroku using Code Institute's mock terminal to run.
This project has been designed for educational purposes 

Users are welcomed by the main menu where they enter name and city before being brought to the main menu where they can choose option 1 to start the game or option 2 to view instructions (Q to Quit). 

After choosing to start the game they are type in their name and city .
Users are given the option to start with a default balance of €100 or change it to pre-defined amount or set it manually hence change difficulty level.

Next, users are asked to choose the number of lines they wish to bet on (1-3). The more lines the bigger chance of winning, however, the user bet is then multiplied by the number of lines the user wishes to bet on and deducted from the total balance. Once, users choose the number of lines to bet on, this information is confirmed and printed back to the screen. 

Users then are asked to type in how much would they like to bet per line - this information is also confirmed and printed back to users unless the balance is insufficient to cover the bet. in this instance, users are asked to repeat and choose the number of lines to bet on and confirm bet per line.

Once lines and bet are confirmed, users are presented with the information of their bet total, results of the round and lines and amount they won/lost on. 

The total balance is then adjusted and, if allowed to play, users are asked to play another round. 
If a user loses the whole balance, the game is over and users are brought back to the main menu.

You can view the live, deployed application here: <a href ='https://shemmy-slot-mashine.herokuapp.com/' target="_blank">One-Armed Bandit!</a>


![One-Armed Bandit! image](assets/images/am-i-responsive.png)

## __Live Web-Page__
[One-Armed Bandit!](https://shemmy-slot-mashine.herokuapp.com/)

## __GitHub Repository__
[GitHub Repository](https://github.com/ShemmyYo/slot-mashine-python/)

## __Tech Stack__

<img height="45" src="assets\images\python-icon.png"> __Python3__ 
<img height="50" src="assets\images\gitpod.png"> __Gitpod__ 
<img height="45" src="assets\images\github.png"> __Git__

<img height="42" src="assets\images\html.png"> __HTML5__
<img height="50" src="assets\images\css-img.png"> __CSS3__

***

# Contents

- [Project Goal](#project-goal)
- [Brief](#brief)
- [UX User Experience](#ux-user-experience)
    - [User Stories](#user-stories)
    - [Flowchart](#flowchart)
    - [Colour Scheme](#colour-scheme)
    - [Class Object](#classobject)
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Main Menu](#main-menu)
        - [Instructions](#home)
        - [High-Scores](#highscores)
        - [Deposit Change Option](#deposit)
        - [Setting lines to bet on and bet mount (difficulty level)](#difficulty)
        - [Turn results](#turn-results)
        - [Game Over](#game-over)
- [Technologies Used](#technologies-used)
    - [Imported Libraries and Packages](#libraries-imported)
    - [Data Model](#data-model)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Deploy to Heroku](#deploy-to-heroku)
    - [Local Deployment](#local-deployment)
    - [To Fork the Repository](#to-fork-the-repository)
- [Credits](#credits)
    - [Code](#code)
    - [Design](#design)
    - [Acknowledgements](#acknowledgements)

***
## __Project Goals__

The project goal was to create a user-friendly game and deliver an easy and satisfiying command line interface directory.

The project has been built by using Python.

[Back to Content](<#contents>)
***
## __Brief__

I wish to demonstrate my competency as a Software Developer and showcase Python skills and abilities to potential Employers / Recruiters and all who want to cooperate with me on future projects.

[Back to Content](<#contents>)
***
## __UX User Experience__
### __User Stories__

__As a Player, I wish:__ 

|     |                                   ACTION                                   |
| --- | :------------------------------------------------------------------------: |
| 1   | to play a simple and fun but still challenging game.                       |
| 2   | to be able to see instructions before the start of the game.               |
| 3   | to play a game that navigates easyly.                                      |
| 4   | to be able to set bet amount.                                              |
| 5   | to be able to change game difficulty by changing number of lines I bet on. |
| 6   | to be given feedback if I entered invalid data.                            |
| 7   | to be able to go reset the game.                                           |
| 8   | to be able to see current balance.                                         |
| 9   | to be encouraged to replay and increase scores.                            |
| 10  | to check if user made the top 10 high-scores.                              |

[Back to Content](<#contents>)
***
### __Flowchart__

The below flowchart has been created prior to my code to give me a clear view of what needed to be implemented. It clearly indicates the layout and structure of the program including where the user needs to be asked for input, where the computer validates the input and how to handle invalid inputs, where the program should subtract and add to the user's balance.

![Flowchart](/assets/images/flow-chart.png)

### __Color Scheme__

To provide better user experience, I have decided to use color scheme.
The colors used were from ANSI gamma, as described below:

- Yellow color (\033[1;33;40m)
- Red color (\033[1;31;40m)
- Magenta color (\033[1;35;40m)
- Green color (\033[1;32;40m)
- Blue color (\033[1;34;40m)

### __Class Object__
OOC (Object Oriented Class) has been added in this project to create a Player class.
I used [Real Python](https://realpython.com/python3-object-oriented-programming/) to create it.

```python
class Player:
    def __init__(self, name, place, rounds, balance, wins, win):
        self.name = name
        self.place = place
        self.rounds = 0
        self.balance = DEPOSIT
        self.wins = 0
        self.win = 0
```

[Back to top](<#contents>)
***

## __Features__
### __Welcome Screen__
The user is welcomed to the game wtih game logo and prompted to input their details.

![Welcome screen image](assets/images/slot-mashine-screen.png)

<details><summary>Player Info IMAGE</summary>

![Player Info](assets/images/player-info.png)
</details>

***

### __Main Menu__
Main menu enables the user to start the game, view the game instructions, high-scores and exit the game.

<details><summary>Main Menu IMAGE</summary>

![Main Menu](assets/images/main-menu.png)
</details>

***

### __Instructions__
Option 2 on main menu displays game instructions. 
You can come back to the main menu by hitting the Enter key or quit by hitting Q key.

<details><summary>Instructions IMAGE</summary>

![Instructions](assets/images/instructions.png)
</details>

***

### __High-Sores__
Option 3 on main menu displays top 10 High-Scores. 
You can come back to the main menu by hitting the Enter key.

<details><summary>High-Scores IMAGE</summary>

![Instructions](assets/images/high-scores.png)
</details>

***

### __Deposit change option (difficulty level)__
Changing deposit may make the game easier (if set to higher) or more diffcult (if set lower)

<details><summary>Deposit Change Option IMAGE</summary>

![Deposit Change Option](assets/images/deposit.png)
</details>

***

### __Setting lines to bet on and bet mount (difficulty level)__
Users can set the number of lines (1-3) to bet on and bet amount which makes the game easier (if set to 3 lines) or more diffcult (if set 1 lines)

<details><summary>Setting lines and bet IMAGE</summary>

![Setting lines and bet](assets/images/lines-bet.png)
</details>

***

### __Turn results__
Reluts are presented in grapicly on reels (same way as on a real one-armed bandid).
Each line is analised and results for each line is printed (includin the amount won/lost and number of winning/loosing lines)

<details><summary>Results IMAGE</summary>

![Results](assets/images/turn-results.png)
</details>

***

### __Progress Bar__
Added for visual enhancement. 

<details><summary>Progress Bar IMAGE</summary>

![Progress Bar](assets/images/progress-bar.png)
</details>

***

### __Game Over__
Showing final result of the game.
Final score will be checked against the current 10 highests scores.
Regardless of whether user gets to top 10 or not, high-scores table is updated and displayed. 

<details><summary>Game Over IMAGE</summary>

![Game Over](assets/images/game-over.png)
</details>

[Back to Content](<#contents>)

***
## __Technologies Used__

- [Python](https://www.python.org/) - To provide the functionality to the program
- [Heroku](https://dashboard.heroku.com/apps) Used to deploy application.
- [HTML5](https://html.spec.whatwg.org/) - provides content and structure 
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) - provides styling 
- [MindManager](https://app.mindmanager.com/) - for Flowcharts
- [Aurora Gradient Animation](https://dev.to/albertwalicki/aurora-ui-how-to-create-with-css-4b6g) - created Aurora gradient background for website
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - used extensively to experiment with grid, flexbox and general responsiveness
- [Gitpod](https://www.gitpod.io/) - used to create and host the website
- [Github](https://github.com/) - used to deploy the website 
- [Git](https://git-scm.com/) - used for version control through the Gitpod terminal
- [Am I Responsive](https://ui.dev/amiresponsive) - to create an image displaying the home page on various devices 
- [Grammarly](https://app.grammarly.com/) - to make writing clear and engaging as well as eliminate grammar errors
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [PyInputPlus](https://pypi.org/project/PyInputPlus/) - used to validate user inputs

### __Imported Libraries and Packages__

- [random](https://docs.python.org/3/library/random.html) was used to select symbols for reels
- [os](https://docs.python.org/3/library/os.html) was used to create the clear_screen function to enhance user experience and reduce clutter on screen
- [time](https://docs.python.org/3/library/time.html) used time.sleep to enhance user experience and to pause
- [gspread](https://docs.gspread.org/en/v5.7.0/) for linking Google Sheets to read and update high-scores table.
- [Google Auth](https://google-auth.readthedocs.io/en/master/) to access Google Sheets
***
- [colorama](https://pypi.org/project/colorama/) allows terminal text to be printed in different colors

[Back to Content](<#contents>)

***

### __Data Model___

I used Google Sheets to store high-scores data. 

![Google Sheets](assets/images/google-sheets.png)

***

## __Testing__
### __PEP8 CI Validation__

Online validation tool (provided by CI) was used to check that the code is up to standard.
All validated with no errors.

[PEP8CI](https://pep8ci.herokuapp.com/) 

![PEP8 CI Validation](assets/images/pep8.png)

### __Tests based on user stories:__

|     |                                   ACTION                     | Requirement met |
| --- | :----------------------------------------------------------: | :-------------: |
| 1   | to play a simple and fun but still challenging game.         | Yes             |
| 2   | to be able to see instructions before the start of the game. | Yes             |
| 3   | to play a game that navigates easyly.                        | Yes             |
| 4   | to be able to set bet amount.                                | Yes             |
| 5   | to be able to change game difficulty by changing number of lines I bet on.  | Yes             |
| 6   | to be given feedback if I entered invalid data.              | Yes             |
| 7   | to be able to go reset the game.                             | Yes             |
| 8   | to be able to see current balance.                           | Yes             |
| 9   | to be encouraged to replay and increase scores.              | Yes             |
| 10  | to check if user made the top 10 high-scores.                | Yes             |

***

__Manual tests:__
- Verified ....................

[Back to Content](<#contents>)

***

## __Deployment__
### __Deploy to Heroku__

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

***

### __Local Deployment__

To make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/shemmyyo/slot-mashine-python.git`

***

### __To Fork the Repository__

To make a copy or ‘fork’ the repository - 

1. Log into GitHub and locate the repository  
2. On the right-hand side of the page select the ‘fork’ option to create and copy the original

Alternatively, if using Gitpod, you can click below to create your workspace using this repository

[Back to Content](<#contents>)

***

## __Credits__

- Throughout the building process I found many helpful tutorials online.
I sometimes applied principles within them to the site, after fully understanding their code and modifying to fit the site's needs.

- Heroku deployment instructions from Code Institute
GitHub Python Template [Code Institute](https://codeinstitute.net/)

### __Code__

- Tutorial that helped me figure out the logic for the game [Tech With Tim](https://www.youtube.com/watch?v=th4OBktqK1I)

- Code to create clear_screen function taken from [GeeksforGeeks](https://www.geeksforgeeks.org/clear-screen-python/)

- Inspiration and code for progress bar [StackOverflow](https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters/13685020)

- random library [Docs Python](https://docs.python.org/3/library/random.html)

- os library [Docs Python](https://docs.python.org/3/library/os.path.html)

- datetime library [Docs Python](https://docs.python.org/3/library/datetime.html)

### __Design__

- Flowchart was made using [MindManager](https://app.mindmanager.com/)

- Inspiration for gradient HTML/CSS background [Aurora UI](https://dev.to/albertwalicki/aurora-ui-how-to-create-with-css-4b6g) 


### __Acknowledgements__

As always, big thank you to [Harry Dhillon](https://github.com/Harry-Leepz), my mentor who provided me with guide and excellent feedback throughout the project

***

One-Armed Bandit! was developed for educational purpouses and as part of my Diploma in Software Development with [Code Institute](https://codeinstitute.net/). 


Shemmy, 2022


[Back to top](<#project-portfolio-3---python>)