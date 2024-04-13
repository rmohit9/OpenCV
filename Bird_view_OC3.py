import cv2
import numpy as np

img= cv2.imread(r"C:\Users\Dell\OneDrive\Desktop\git\Resources\card.jpg")

pts1= np.float32([[460,84],[578,183],[313,262],[430,360]])
print(pts1)

for x in range (0,4):
    cv2.circle(img,(pts1[x][0], pts1[x][1]),5,(0,0,255),cv2.FILLED)
#          image with pixels      ,radius,color,thickness(filled)

cv2.imshow("Original Image",img)
cv2.waitKey(0)