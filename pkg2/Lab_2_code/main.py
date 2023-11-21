import cv2 as cv
import numpy as np
import matplotlib as plt
from tkinter import *

def select_image():
	# grab a reference to the image panels
	global panelA, panelB
	# open a file chooser dialog and allow the user to select an input
	# image
	path = tkFileDialog.askopenfilename()


img1 = cv.imread("examples/kitties.jpg")
img2 = cv.imread("examples/minecraft.png")
img3 = cv.imread("examples/saw.jpg")
img4 = cv.imread("examples/cats.gif")


window = Tk()
window.title("Images")
window.mainloop()
btn = Button(root, text="Select an image", command=select_image)

cv.imshow("Display window", img1)
k = cv.waitKey(0)