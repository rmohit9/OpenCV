import cv2
import numpy as np

# Set the width and height of the frame
frameWidth = 640
frameHeight = 480

# Open the webcam (default camera index is 0)
cap = cv2.VideoCapture(0)

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)


def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)



# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Failed to open webcam.")
else:
    while True:
        # Read a frame from the webcam
        ret, img = cap.read()

        imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
        h_min =cv2.getTrackbarPos("HUE Min","HSV")
        h_max =cv2.getTrackbarPos("HUE Max","HSV")
        s_min =cv2.getTrackbarPos("SAT Min","HSV")
        s_max =cv2.getTrackbarPos("SAT Max","HSV")
        v_min =cv2.getTrackbarPos("VALUE Min","HSV")
        v_max =cv2.getTrackbarPos("VALUE Max","HSV")
        print(h_min)
        
        
        lower =np.array([h_min,s_min,v_min])
        upper =np.array([h_max,s_max,v_max])
        mask =cv2.inRange(imgHsv,lower,upper)
        result = cv2.bitwise_and(img,img,mask = mask)
        
        mask =cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
        hStack = np.hstack([img,mask,result])
        
        
        
        
        cv2.imshow('Webcam', img)
        cv2.imshow('HSV Color Space', imgHsv)
        cv2.imshow('Mask', mask)
        cv2.imshow('Results=', result)
        cv2.imshow("Horizontal Stacking",hStack)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()
