import cv2
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import time as tp

# Disable scientific notation for clarityr
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model_bool_2.h5", compile=False)

# Load the label
class_names = open("labels_bool.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# video_path = "Datasets/video1.mp4"
video_path = "Datasets/video2_fast.mp4"

# Open the video files
cap = cv2.VideoCapture(video_path)
# cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame = cap.read()

while ret:
    # Convert the frame from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the NumPy array to PIL Image
    image = Image.fromarray(rgb_frame)
    
    # Resize the frame to be at least 224x224 and then crop from the center
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # Convert the image to a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

    # Read the next frame
    ret, frame = cap.read()


    # Use the putText function to draw text on the image
    cv2.putText(frame, "Class: {}".format(class_name[2:]), (855, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    cv2.putText(frame, "Confidence Score: {:.1f}%".format(confidence_score*100), (855, 125), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    cv2.imshow('frame', frame)

    tp.sleep(0.03)

     # set the condition of manual brake by pressing "k" on the keyboard  
    if cv2.waitKey(1) & 0xFF==ord("k"):
        break

# Release the video capture object
cap.release()





