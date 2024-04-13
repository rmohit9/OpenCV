# #Crop and Resize

# import cv2
# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path)
# print(img.shape)

# width ,height =1000, 1000
# imgResize =cv2.resize(img,(width,height))
# print(imgResize.shape)

# imgCropped =img[25:225,230:370]
# print(imgCropped.shape)

# imgCroppedResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
#                                           #width       height

# cv2.imshow("Lena",img)
# # cv2.imshow("Lena Resized",imgResize)    
# cv2.imshow("Lena Cropped",imgCropped)
# cv2.imshow("Lena Cropped resize",imgCroppedResize)
# cv2.waitKey(0)



# #COLORING THE IMAGE 
# import cv2
# import numpy as np

# img= np.zeros((512,512,3),np.uint8)
#              #(matrix,matrix,color channel)
# print(img)
# img[:] =0,0,255
##Taking whole image=B,G,R
# cv2.imshow("Image",img)

# cv2.waitKey(0) 


# #DRAWLING THE LINE , SHAPES ,TEXT
# import cv2
# import numpy as np

# img= np.zeros((512,512,3),np.uint8)
#              #(matrix,matrix,color channel)
# print(img)

# cv2.line(img,(0,0),(500,500),(0,0,255),2)
#         #     pt.1, pt.2    , B,G,R   ,thickness
# cv2.rectangle(img,(350,50),(450,100),(0,255,0),cv2.FILLED)
#         #     pt.1, pt.2    , B,G,R   ,thickness(filled)
# cv2.circle(img,(150,400),100,(255,0,0),cv2.FILLED)
#         #     centre pt,radius,B,G,R   ,thickness(filled)
# cv2.putText(img,"Text Here",(75,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,0,255))
#         #                   Position,   Font                   ,scale,(B,G,R)

# cv2.imshow("Image",img)
# cv2.waitKey(0)



# #JOIN ALL IMAGES
# import cv2
# import numpy as np
# import Join_images


# kernel =np.ones((5,5),np.uint8)
# print (kernel)

# path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
# img = cv2.imread(path) # to read the image 
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny =cv2.Canny(imgBlur,100,100)
# imgDilation =cv2.dilate(imgCanny,kernel, iterations=1)   #it is no iteration of the dilation on image 
# imgEroded =cv2.erode(imgDilation,kernel, iterations=1)

# StackedImages =Join_images.stackImages(0.8,([img,imgGray,imgBlur],[imgCanny,imgDilation,imgEroded]))
# cv2.imshow("Stacked Images",StackedImages)

# # cv2.imshow("mail", img) 
# # cv2.imshow("grayscale", imgGray) # to show the image 
# # cv2.imshow("Image Blur", imgBlur)
# # cv2.imshow("Image Canny", imgCanny)
# # cv2.imshow("Image dilation", imgDilation)
# # cv2.imshow("Image Erosion", imgEroded)
# cv2.waitKey(0)





# # JOIN ALLL WEBCAMS

# import cv2
# import numpy as np
# # import Join_images

# def stackImages(scale,imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range ( 0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale,scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor = np.hstack(imgArray)
#         ver = hor
#     return ver

# frameWidth =640 
# frameHeight =100

# cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

# while True:
#     sucess,img=cap.read()
#     # cv2.imshow ("Video",img)

#     kernel =np.ones((5,5),np.uint8)
#     print (kernel)

#     # path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
#     # img = cv2.imread(path) # to read the image 
#     imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#     imgCanny =cv2.Canny(imgBlur,100,100)
#     imgDilation =cv2.dilate(imgCanny,kernel, iterations=1)   #it is no iteration of the dilation on image 
#     imgEroded =cv2.erode(imgDilation,kernel, iterations=1)

#     StackedImages =stackImages(0.3,([img,imgGray,imgBlur,img,imgGray,imgBlur],
#                                     [imgCanny,imgDilation,imgEroded,imgCanny,imgDilation,imgEroded],
#                                     [img,imgGray,imgBlur,img,imgGray,imgBlur],
#                                     [imgCanny,imgDilation,imgEroded,imgCanny,imgDilation,imgEroded],
#                                     [img,imgGray,imgBlur,img,imgGray,imgBlur],
#                                     [imgCanny,imgDilation,imgEroded,imgCanny,imgDilation,imgEroded]
#                                     ))
#     cv2.imshow("Stacked Images",StackedImages)

#     # cv2.imshow("mail", img) 
#     # cv2.imshow("grayscale", imgGray) # to show the image 
#     # cv2.imshow("Image Blur", imgBlur)
#     # cv2.imshow("Image Canny", imgCanny)
#     # cv2.imshow("Image dilation", imgDilation)
#     # cv2.imshow("Image Erosion", imgEroded)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break






#USING IMPORT JOIN IMAGES FUNCTION
import cv2
import numpy as np
import Join_images



frameWidth =640 
frameHeight =100

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    sucess,img=cap.read()
    # cv2.imshow ("Video",img)

    kernel =np.ones((5,5),np.uint8)
    print (kernel)

    # path=r"C:\Users\Dell\OneDrive\Desktop\git\Resources\Lena.jpg"
    # img = cv2.imread(path) # to read the image 
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
    imgCanny =cv2.Canny(imgBlur,100,100)
    imgDilation =cv2.dilate(imgCanny,kernel, iterations=1)   #it is no iteration of the dilation on image 
    imgEroded =cv2.erode(imgDilation,kernel, iterations=1)

    StackedImages =Join_images.stackImages(0.3,([img,imgGray,imgBlur,img,imgGray,imgBlur],
                                    [imgCanny,imgDilation,imgEroded,imgCanny,imgDilation,imgEroded],
                                    [img,imgGray,imgBlur,img,imgGray,imgBlur],
                                    [imgCanny,imgDilation,imgEroded,imgCanny,imgDilation,imgEroded],
                                    [img,imgGray,imgBlur,img,imgGray,imgBlur],
                                    [imgCanny,imgDilation,imgEroded,imgCanny,imgDilation,imgEroded]
                                    ))
    cv2.imshow("Stacked Images",StackedImages)

    # cv2.imshow("mail", img) 
    # cv2.imshow("grayscale", imgGray) # to show the image 
    # cv2.imshow("Image Blur", imgBlur)
    # cv2.imshow("Image Canny", imgCanny)
    # cv2.imshow("Image dilation", imgDilation)
    # cv2.imshow("Image Erosion", imgEroded)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break