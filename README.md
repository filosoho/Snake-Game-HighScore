# Snake Game
A simple Snake Game recording the High Score, implemented in Python using the Turtle graphics library. This is an upgraded version of Snake-Game.

# How to Play
Simply run the game by executing the:
~~~
main.py
~~~
in a Python environment.  

Use the arrow keys to control the snake:  
* Up arrow: Move the snake up  
* Down arrow: Move the snake down  
* Left arrow: Move the snake left  
* Right arrow: Move the snake right  

The objective of the game is to eat the food that appears on the screen and grow as long as possible without hitting the walls or colliding with the snake's own body. The game ends if the snake hits the wall or collides with its own body.  
* The game can be paused by pressing the 'p' key and resumed by pressing it again.  
* The game can be closed by pressing the 'e' key.   

The player's current score and the highest score achieved so far are displayed on the screen.  

The highest score is saved in a file called data.txt and will be updated if a new high score is achieved.  


# Game Components
The game consists of the following components:
~~~
Snake: 
The snake is controlled by the player and moves around the screen. 
The player must navigate the snake to eat the food and avoid hitting the walls or colliding with its own body.   
The snake grows longer each time it eats food.


Food: 
The food appears at random locations on the screen. The snake must eat the food to grow longer and increase the player's score.


Scoreboard: 
The scoreboard displays the player's current score and the highest score achieved so far.   
The highest score is saved in a file called data.txt and will be updated if a new high score is achieved.  
~~~

# Game Features
* The game window has a width of 600 pixels and a height of 600 pixels, with a gray background color.  

* The snake is initially positioned at the center of the screen and starts moving to the right.  

* The food appears at random locations on the screen with a random shape and color.  

* The snake's movement speed can be adjusted by changing the value of the time.sleep() function.  

* The game can be paused by pressing the 'p' key, and the game can be closed by pressing the 'e' key.  

* The game keeps track of the player's current score and updates the scoreboard accordingly.  

* The game ends if the snake hits the walls or collides with its own body. The game resumes and the player is given the option to play again or stop the game by pressing 'e' and clicking on the screen to close it.  

* If the player achieves a new high score, it is saved in a file called data.txt.  

# Dependencies
The game requires the:
~~~
turtle library
~~~
which is a standard library in Python and does not require any additional installation.

# How to Run the Game
Clone or download the repository to your local machine.  
Open a Python environment and navigate to the directory where the game files are located.  
Run the:
~~~
main.py 
~~~
script using the Python interpreter.  
The game window should open, and you can start playing the game by following the instructions provided in the game.

# Interface  

<br>

![Snake Game High Score](https://github.com/filosoho/Snake-Game-HighScore/blob/c3b2d827942da650849e09fc7c2086d6ce6da938/1.png) 

![Snake Game High Score](https://github.com/filosoho/Snake-Game-HighScore/blob/c3b2d827942da650849e09fc7c2086d6ce6da938/2.png)

![Snake Game High Score](https://github.com/filosoho/Snake-Game-HighScore/blob/c3b2d827942da650849e09fc7c2086d6ce6da938/3.png)

<br>

# Contributing
If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License
Feel free to use and modify the code as per your requirements. 
