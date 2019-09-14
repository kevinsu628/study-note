import cv2
import matplotlib as plt

# reading a video
filename = "/Users/kevinsu/Desktop/Ascent/Udacity/CarND/CarND-Advanced-Lane-Lines/output_images/project_video_output.mp4"

cv2.namedWindow("sample video", cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(filename)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow('sample video', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()