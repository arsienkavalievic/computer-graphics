import cv2 as cv
import numpy as np
import matplotlib as plt

img = cv.imread("examples/kitties.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window