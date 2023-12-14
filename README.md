# Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera. 

## Milestone 1 

- Creates a remote github repository for this project to version control the software.

- Connects the remote repository to a local clone using the command line.

```bash
git clone git clone https://github.com/d4min/computer-vision-rock-paper-scissors.git
```

## Milestone 2

- Created and trained a deep learning model using Teachable Machine to recognise images of users gesturing rock, paper, scissors or nothing through the webcam. 

![Screenshot](images/TeachableMachine.png)

## Milestone 3

- Used conda to create and install the dependencies required for the project.

- First created a new virtual environment with conda where the dependencies would be installed. 

```bash
conda create --name computer_vision python
```
It is important to use an environment seperate from base becasue virtual environments let you have a stable, reproducible, and portable environment. You are in control of which packages versions are installed and when they are upgraded. You can have as many environments as you want and this reduces the likelihood of dependencies between projects clashing and causing errors. 

```bash
conda install pip
conda install tensorflow opencv ipykernel
```
- I also exported the conda environment packages to a text file which is kept with the code to allow for other users to be able to install the required dependencies to work with the project.

```bash
conda list --explicit > requirements.txt
```

## Milestone 4

- Wrote the script manual_rps.py which is a manual version of the intended program which takes in a user choice through text and then picks the computer choice randomly from a list of choices. 

- Defined functions for taking the user choice as well as choosing the computer choice. 

```python
def get_computer_choice():
    rps  = ['Rock', 'Paper', 'Scissors']
    return random.choice(rps)
```
This uses the random library to pick a random item from the rps list and then returns the computer choice. 

```python
def get_user_choice():
    user_choice = input('Please enter rock, paper or scissors')
    return user_choice.capitalize()
```
Gets user input through a prompt, returns the input capitalised to ensure it is the right format for the rest of the script. 

- Used if else statements to determine the winner of the game by comparing the computer choice to the user choice. 

```python
def get_winner(computer_choice, user_choice):
    winner = ''
    if computer_choice == user_choice:
        print('It is a tie!')
        winner = 'Tie'
        ...
        ...
        ...
```
The above code shows a slice of the entire function which determines the winner. The function returns the winner of the game. 