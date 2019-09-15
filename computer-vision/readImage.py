import cv2
import matplotlib as plt
import numpy as np

##############################################################################
# display an image
def readImage(img):
    # default 0: fit the image's size
    # if WINDOW_AUTOSIZE flag: auto resize as image gets resized by users
    cv2.namedWindow("sample", cv2.WINDOW_AUTOSIZE)
    if img.any() == None:
        print("Bad image")

    cv2.imshow("sample", img)

    # wait key stroke indefenitely
    # if positive number n passed in, wait n millisecond
    cv2.waitKey(0)
    cv2.destroyWindow("sample")

##############################################################################
def blurredImage(img):
    # add some blurs
    # create a out image
    out = np.empty_like(img)
    blured_img = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=3, sigmaY=3, dst=out)
    cv2.imshow("sample", out)
    cv2.waitKey(0)
    cv2.destroyWindow("sample")

##############################################################################
def grayscaleImage(img):
    # use Canny edge detector writedd outputs to grayscale
    img_rgb = np.empty_like(img)
    img_gray = np.empty_like(img)
    img_cny = np.empty_like(img)

    cv2.namedWindow("example gray", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("example canny", cv2.WINDOW_AUTOSIZE)

    img_rgb = img
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    cv2.imshow("example gray", img_gray)
    img_cny = cv2.Canny(img_gray, 10, 100, L2gradient=True)
    cv2.imshow("example canny", img_cny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

##############################################################################
def downsampleImage(img):
    # down sample by 2
    img_pyr = cv2.pyrDown(src=img)
    img_cny = cv2.Canny(img_pyr, 10, 100, L2gradient=True)
    cv2.imshow("example gray", img_cny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

filename = "./3.jpg"
img = cv2.imread(filename)
readImage(img)
blurredImage(img)
grayscaleImage(img)
downsampleImage(img)
cv2.destroyAllWindows()



