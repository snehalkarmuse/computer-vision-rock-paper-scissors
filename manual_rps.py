import random

def get_computer_choice():
    random_choice = ["Rock","Paper","Scissors"]
    return random.choice(random_choice)


def get_user_choice():
    user_choice = input("Please choose from Rock, paper and Scissor: ")
    return user_choice

comp_choice = get_computer_choice()
user_choice = get_user_choice()
print("computer choice: ",comp_choice)
print("User choice: ", user_choice)
