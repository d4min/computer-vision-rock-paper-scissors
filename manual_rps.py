import random 

def get_computer_choice():
    rps  = ['Rock', 'Paper', 'Scissors']
    return random.choice(rps)

def get_user_choice():
    user_choice = input('Please enter rock, paper or scissors')
    return user_choice.capitalize()