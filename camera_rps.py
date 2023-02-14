import cv2
from keras.models import load_model
import numpy as np
import time
from datetime import datetime, timedelta
import random

class RockPaperScissor:
    def __init__(self):
        self.computer_win = 0
        self.user_win = 0
        self.play_count = 0
        self.computer_choice = None
        self.user_choice = None

    def play(self):
        while (self.play_count < 5) and (self.user_win < 3) and (self.computer_win < 3) :
            self.computer_choice = self.get_computer_choice()
            self.user_choice  = self.get_user_choice()
            self.check_winner()
            self.play_count = self.play_count + 1
            print("Play count: ",self.play_count,"computer choice :", self.computer_choice, "User choice: ", self.user_choice)

    
        

    def get_computer_choice(self):
        self.computer_choice = ["Rock","Paper","Scissor","Nothing"]
        return random.choice(self.computer_choice)
    
    def get_user_choice(self):
        predicted_result = self.get_prediction()
        print(" result : ",predicted_result[0])
        max_num = 0
        for i in predicted_result[0]:
            if i > max_num:
                max_num = i
                print(type(max_num), max_num)
        result_tp = np.where(predicted_result[0] == max_num)
        index_number = result_tp[0][0]
        print(index_number)

        if index_number == 0:
            
            self.user_choice = "Rock"
        elif index_number == 1:
           
            self.user_choice = "Paper"
        elif index_number == 2:
            
            self.user_choice = "Scissor"
        else:
            
            self.user_choice = "Nothing"
        return self.user_choice
    
    def get_prediction(self):
        now = time.time() # gets the current second to start countdown
        future_time = now + 5    # adding   5 seconds in current time
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while now <= future_time:           # comparing current time and future time in seconds
            now = time.time()               # changing value of now 

            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            self.prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            # print(self.prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            #After the loop release the cap object
            cap.release()
            # Destroy all the windows
            cv2.destroyAllWindows()          
            #print("You chose rock.")
        return self.prediction
    
    def check_winner(self):
        self.user_choice = self.user_choice.capitalize()

        if self.computer_choice == self.user_choice:
                #print("It is a tie!")
                print(f"Computer win: ",{self.computer_win}, "User win: ",{self.user_win})
        elif self.computer_choice == "Rock":
            if self.user_choice == "Paper":
                #print("You won!")
                self.user_win = self.user_win + 1
                print(f"Computer win: ",{self.computer_win}, "User win: ",{self.user_win})
            else:
                #print("You lost")
                self.computer_win = self.computer_win + 1
                print(f"Computer win: ",{self.computer_win}, "User win: ",{self.user_win})
        elif self.computer_choice == "Paper":
            if self.user_choice == "Scissor":
                #print("You won!")
                self.user_win = self.user_win + 1
                print(f"Computer win: ",{self.computer_win}, "User win: ",{self.user_win})
            else:
                #print("You lost")
                self.computer_win = self.computer_win + 1
                print(f"Computer win: ",{self.computer_win}, "User win: ",{self.user_win})
        elif self.computer_choice == "Scissor":
            if self.user_choice == "Rock":
                #print("You won!")
                self.user_win = self.user_win + 1
                print(f"Computer win: ",{self.computer_win}, "User win: ",{self.user_win})
            else:
                #print("You lost")
                self.computer_win = self.computer_win + 1
                print(f"Computer win: ",{self.computer_win}, "User win: ",{self.user_win})
        else:
            print("Enter your choice.")
        

    

rps_game = RockPaperScissor()
rps_game.play()





           

