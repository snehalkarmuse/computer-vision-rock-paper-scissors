# Computer Vision RPS
This project is regarding machine learning. Playing a game called Rock Paper and Scissor. Giving visual command to computer as a input.
## Milestone 2
- In milestone 2, creates a model using Teachable-Machine. 
- Teachable-Machine is web based tool which creates machine model easily. It is accessible to anyone.
- creats four classes Rock, Paper, Scissor and Nothing. Stores as many as images in each classes using identify the hand movement.
- Stores various imgages for rock, paper, scissor and nothing. It helps to identify any position for above classes.
- After this train the machine( get use to with each images and falls in which class.)
- Finishes with export the model. 
- In this export model opens a new window where Tensorflow creates kernel_model.h5 and label.txt file. Which is nothing but python code for machine to undderstand the image.
## Milestone 3
- install the dependencies.
- creates the environment ready for the game.
- install new enviornment, activate it.
- install pip, panda, tensorflow, ipykernel, opencv-python.
## Milestone 4
- Import the random module.
- Creates four function. get_computer_choice(), get_user_choice(), get_winner(), play().
- In get_computer_choice(), computer randomly chooses option from rock, paper or scissors.
- In get_user_choice(), user chooses from above three options.
- In get_winner(), takes two argument computer_choice and user_choice. compares them using if- elif- else, if they are same then it prints "It's tie". If user chooses scissor and computer chooses rock then prints "You lost" or vice versa. Next condition is, if user chooses paper and computer chooses rock then it prints "You won" else You lost. Last condition is, if user chooses Scissors and computer chooses paper then prints "You won" else "You lost".
- Last function play(), in the body of this function put all above three function.
- called the play()