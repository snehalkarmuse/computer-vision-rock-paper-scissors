![alt text][]

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

### Milestone 5
- In get_prediction(), adds countdown for user to know when the screen going to close. 
- It takes current time using time() from time module.
- Adds 5 sec. in the time.
- Adds while loop to compare current time and future time. saving the current time as a now time.
- Every 5 secs the sceen closes.
- Use puttext() to write a countdown on the screen.
- adds the another functionality, to repeat the game till either computer or user wins. Also game will continue upto 5 times.
- Keep count of win with variables computer_wins and user_wins.
- For above functionality, update play(). Adds while loop to check round of play is less then 5. Inside while checks the        condition count of each player. Accordingly game continues.
- Changed the program layout with class. Creats class called RockPaperScissor. Initilized variables in init method.
- Move all function into the class.
- created instance of the class called rps_game.
- This instance calls play method.