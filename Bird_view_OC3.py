import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Dell\OneDrive\Desktop\git\Resources\card.jpg")

width, height = 250, 350
pts1 = np.float32([[460, 84], [578, 183], [313, 262], [430, 360]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # Destination points for perspective transformation
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Convert pts1 to integer
pts1_int = np.int32(pts1)

# Draw circles
for point in pts1_int:
    cv2.circle(imgOutput, tuple(point), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Original Image", img)
cv2.imshow("Output Image", imgOutput)
cv2.waitKey(0)
