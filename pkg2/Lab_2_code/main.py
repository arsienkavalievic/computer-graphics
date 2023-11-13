import cv2 as cv
import numpy as np

img = cv.imread("path/to/image")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window