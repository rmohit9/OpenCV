import cv2
import numpy as np

circles =np.zeros((4,2),np.int32)
counter =0

def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[counter] = x,y
        counter = counter + 1
        print(circles)

img = cv2.imread(r"C:/Users/Dell/OneDrive/Desktop/git/Resources/premium_photo-1667251760504-096946b820af.jpg")

while True:
    
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # Destination points for perspective transformation
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image",imgOutput)
        # Convert pts1 to integer
        # pts1_int = np.int32(circles)

    # Draw circles
    for x in range (0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]), 5, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image",mousePoints)
    # cv2.imshow("Output Image", imgOutput)
    cv2.waitKey(0)