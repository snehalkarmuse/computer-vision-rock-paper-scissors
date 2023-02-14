import cv2
from keras.models import load_model
import numpy as np
import time
from datetime import datetime, timedelta
def get_prediction():
    now = time.time() # gets the current second to start countdown
    future_time = now + 10       # adding 5 seconds in current time
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
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        #After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()          
        print("You chose rock.")
    return prediction
    
get_prediction()
