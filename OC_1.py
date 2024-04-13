# import cv2

# reading the image 

# img = cv2.imread(r'C:\Users\Dell\OneDrive\Desktop\git\Resources\html_mail.png') # to read the image 
# cv2.imshow("mail", img) # to show the image 
# cv2.waitKey(1000)



# frameWidth =640 
# frameHeight =100

# cap = cv2.VideoCapture(r"C:\Users\Dell\OneDrive\Desktop\git\Resources\the-crow.mp4")

# while True:
#     sucess,img=cap.read()
#     cv2.imshow ("Video",img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# #MAKING THE IMAGE AS GRAYSCALE USING "0"
# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path,0) # to read the image 
# cv2.imshow("mail", img)  
# cv2.waitKey(0)




# # CONVERTING THE IMAGE FROM BGR TO GRAYSCALE
# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path) # to read the image 
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("mail", img) 
# cv2.imshow("grayscale", imgGray) # to show the image 
# cv2.waitKey(0)




# #ADDING THE BLUR EFFECT
# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path) # to read the image 
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

# cv2.imshow("mail", img) 
# cv2.imshow("grayscale", imgGray) # to show the image 
# cv2.imshow("Image Blur", imgBlur)
# cv2.waitKey(0)




# EDGE DETECTOR
# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path) # to read the image 
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny =cv2.Canny(imgBlur,100,100)

# cv2.imshow("mail", img) 
# cv2.imshow("grayscale", imgGray) # to show the image 
# cv2.imshow("Image Blur", imgBlur)
# cv2.imshow("Image Canny", imgCanny)
# cv2.waitKey(0)



# #IMAGE DILATION (use for thickening of the edges)
# import cv2
# import numpy as np

# kernel =np.ones((5,5),np.uint8)
# print (kernel)

# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path) # to read the image 
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny =cv2.Canny(imgBlur,100,100)
# imgDilation =cv2.dilate(imgCanny,kernel, iterations=2)   #it is no iteration of the dilation on image 

# cv2.imshow("mail", img) 
# cv2.imshow("grayscale", imgGray) # to show the image 
# cv2.imshow("Image Blur", imgBlur)
# cv2.imshow("Image Canny", imgCanny)
# cv2.imshow("Image dilation", imgDilation)
# cv2.waitKey(0)



# #IMAGE EROSION (use for making the edges thin)
# import cv2
# import numpy as np

# kernel =np.ones((5,5),np.uint8)
# print (kernel)

# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path) # to read the image 
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny =cv2.Canny(imgBlur,100,100)
# imgDilation =cv2.dilate(imgCanny,kernel, iterations=1)   #it is no iteration of the dilation on image 
# imgEroded =cv2.erode(imgDilation,kernel, iterations=1)

# cv2.imshow("mail", img) 
# cv2.imshow("grayscale", imgGray) # to show the image 
# cv2.imshow("Image Blur", imgBlur)
# cv2.imshow("Image Canny", imgCanny)
# cv2.imshow("Image dilation", imgDilation)
# cv2.imshow("Image Erosion", imgEroded)
# cv2.waitKey(0)




