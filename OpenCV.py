import cv2
import numpy as np
import pandas as pd
#######################################################
## 1. Loading, Reading and Printing the Image
## Reading and Printing a image
img=cv2.imread("Shahrukh.jpg",)
# print(img.shape)
# cv2.imshow('window',img)
# cv2.waitKey(0)

########################################################
## 2. Changing RGB(colourfull) image to Greyscale image
# # converting colourfull image to grey scale
# img_grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Checking the attributes of image
# print(type(img_grey))
# print(img_grey.shape)
# # Printing the manipulated image
# cv2.imshow('window',img_grey)
# cv2.waitKey(0)

########################################################
## 3. Resizing the image
img= cv2.resize(img,(500,500))
# # Printing the manipulated image
# cv2.imshow('windows',img)
# cv2.waitKey(0)

#########################################################
## 4. Changing colurs of image and stacking horizontally
# B G R colourmaps
# imgBlue= img[:,:,0]
# imgGreen= img[:,:,1]
# imgRed= img[:,:,2]
# # Printing the image
# img_new= np.hstack((imgBlue,imgGreen,imgRed))
# cv2.imshow('window',img_new)
# cv2.waitKey(0)

#########################################################
## 5. Flipping an image
# # a). Along x axis
# imgx=cv2.flip(img,0)
# cv2.imshow('window',imgx)
# cv2.waitKey(0)

# # b). Along y axis
# imgy=cv2.flip(img,1)
# cv2.imshow('window',imgy)
# cv2.waitKey(0)

# # c). Along x and y axis
# imgxy=cv2.flip(img,-1)
# cv2.imshow('window',imgxy)
# cv2.waitKey(0)

#########################################################
# ## 6. Cropping an image
# imgcrop= img[250:500,250:500]
# cv2.imshow('window',imgcrop)
# cv2.waitKey(0)

#########################################################
## 7. Saving a file
# imgcrop= img[40:200,200:400]
# cv2.imwrite('imgcrop.png',imgcrop)

#########################################################
## 8. Drawing Shapes
new_img=np.zeros((512,512,3))
# cv2.imshow('window',new_img)
# cv2.waitKey(0)

# 1). Drawing rectangle
# img_rect= cv2.rectangle(new_img,pt1=(10,50),pt2=(200,400),color=(100,0,0),thickness=1)
# cv2.imshow('windows',img_rect)
# cv2.waitKey(0)

# 2). Drawing circle
# img_circle= cv2.circle(new_img,center=(80,80),radius=100,color=(100,0,0),thickness=1)
# cv2.imshow('windows',img_circle)
# cv2.waitKey(0)

# 3). Drawing line
# img_line= cv2.line(new_img,pt1=(0,0),pt2=(512,512),color=(512,512,3),thickness=1)
# cv2.imshow('windows',img_line)
# cv2.waitKey(0)

# 4). Writing text
# img_text= cv2.putText(new_img,text="Python",org=(100,100),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(100,100,3))
# cv2.imshow('windows',img_text)
# cv2.waitKey(0)

#########################################################

## 9. OpenCV Events
# def draw(events,x,y,flags,params):
#     if events==0:
#         print('Mouse Moved')
#     elif events==1:
#         print('Mouse Down Clicked')
#     elif events==4:
#         print('Mouse Up Clicked')
# cv2.namedWindow(winname='window')
# cv2.setMouseCallback(window_name='window',on_mouse=draw)

# while True:
#     cv2.imshow('window',new_img)
#     if cv2.waitKey(1) & 0xFF==ord('x'):
#         break
# cv2.destroyAllWindows()

###########################################################

## 10. Drawing circle in OpenCV Events
# def draw(events,x,y,flags,params):
#     if events==0:
#         # cv2.rectangle(new_img,pt1=(x,y),pt2=(x+50,y+50),color=(100,0,0),thickness=1)
#         cv2.circle(new_img,center=(x,y),radius=30,color=(0,255,0),thickness=1)
# cv2.namedWindow(winname='window')
# cv2.setMouseCallback(window_name='window',on_mouse=draw)

# while True:
#     cv2.imshow('window',new_img)
#     if cv2.waitKey(1) & 0xFF==ord('x'):
#         break
# cv2.destroyAllWindows()

###########################################################

## 11. Drawing rectangle by clicking and dragging
# flag=False
# ix=-1
# iy=-1
# def draw(events,x,y,flags,params):
#     global flag,ix,iy
#     if events==1:                  # mouse down click
#         flag=True
#         ix=x
#         iy=y
#     elif events==0:                # mouse drag
#         if flag==True:
#             cv2.rectangle(new_img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)
#     elif events==4:                # mouse up click
#         flag=False
#         cv2.rectangle(new_img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)

# cv2.namedWindow(winname='window')
# cv2.setMouseCallback(window_name='window',on_mouse=draw)

# while True:
#     cv2.imshow('window',new_img)
#     if cv2.waitKey(1) & 0xFF==ord('x'):
#         break
# cv2.destroyAllWindows()

###########################################################

## 12. Building a cropping tool
# dp_img= cv2.imread('Shahrukh.jpg')
# dp_img= cv2.resize(dp_img,dsize=(500,500))

# flag=False
# ix=-1
# iy=-1
# def crop(event,x,y,flags,params):
#     global flag,ix,iy
#     if event==1:                    # mouse down click
#         flag=True
#         ix=x
#         iy=y
#     # elif event==0:
#     #     if flag==True:                  # mouse dragging
#     #         cv2.rectangle(dp_img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)
#     elif event==4:
#         flag=False
#         cv2.rectangle(dp_img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)

#         #cropping tool
#         fx=x
#         fy=y
#         cropped=dp_img[iy:fy,ix:fx]
#         cv2.imshow('new_window',cropped)
#         cv2.waitKey(0)

# cv2.namedWindow(winname='window')
# cv2.setMouseCallback(window_name='window',on_mouse=crop)


# while True:
#     cv2.imshow('window',dp_img)
#     if cv2.waitKey(1) & 0xFF==ord('x'):
#         break
# cv2.destroyAllWindows()

###########################################################

## 13. Working with videos (loading coloured video)
# cap= cv2.VideoCapture(0)
# while True:
#     ret,frame=cap.read()
#     cv2.imshow('webcam',frame)

#     if cv2.waitKey(1) & 0xFF==ord('x'):
#         break
# cv2.destroyAllWindows()

###########################################################

## 14. Working with videos (loading B&W video)
cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    video_grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam',video_grey)

    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
cv2.destroyAllWindows()





















