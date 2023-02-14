import random

def get_computer_choice():
    computer_choice = ["Rock","Paper","Scissors"]
    return random.choice(computer_choice)


def get_user_choice():
    user_choice = input("Please choose from Rock, paper and Scissor: ")
    user_choice = user_choice.capitalize()
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
            print("It is a tie!")
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
        else:
            print("You lost!")
    elif computer_choice == "Paper":
        if user_choice == "Scissor":
            print("You won!")
        else:
            print("You lost!")
    elif computer_choice == "Scissor":
        if user_choice == "Rock":
            print("You won!")
        else:
            print("You lost!")
            




    
computer_choice = get_computer_choice()
user_choice = get_user_choice()
print("computer choice: ",computer_choice)
print("User choice: ", user_choice)
get_winner(computer_choice,user_choice)
