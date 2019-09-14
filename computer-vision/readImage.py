import cv2
import matplotlib as plt

# display an image
filename = "./3.jpg"

img = cv2.imread(filename)
# default 0: fit the image's size
# if WINDOW_AUTOSIZE flag: auto resize as image gets resized by users
cv2.namedWindow("sample", cv2.WINDOW_AUTOSIZE)
if img.any() == None:
    print("Bad image")

cv2.imshow("sample", img)

# wait keyy stroke indefenitely
# if positive number n passed in, wait n millisecond
cv2.waitKey(0)
cv2.destroyWindow("sample")