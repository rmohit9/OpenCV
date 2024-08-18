import cv2
import numpy as np

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img=cv2.imread("C:/Users/Dell/OneDrive/Desktop/git/Resources/premium_photo-1667251760504-096946b820af.jpg")
cv2.imshow("Original Image",img)
cv2.setMouseCallback("Original Image",mousePoints)

cv2.waitKey(0)