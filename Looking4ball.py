import cv2 as cv
import imutils
import numpy as np
import time

cam = cv.VideoCapture(0)
counter = 0
while cam.isOpened():
    if counter % 5 == 0:
        ret, frame = cam.read()
        Gaussian_Blur = cv.GaussianBlur(frame , (11,11),0)
        g_img = cv.cvtColor(Gaussian_Blur,cv.COLOR_BGR2GRAY)
        circles = cv.HoughCircles(g_img,cv.HOUGH_GRADIENT,1,20,
                         param1=50,param2=25,minRadius=0,maxRadius=0)
        try:
            for i in circles[0,:]:
            # draw the outer circle
                cv.circle(frame,(int(i[0]),int(i[1])),int(i[2]),(0,255,0),2)
                # draw the center of the circle
                cv.circle(frame,(int(i[0]),int(i[1])),2,(0,0,255),3)
        except:
            pass
        cv.imshow('frame',frame)
        # cv.imshow('median blur',Gaussian_Blur)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    counter +=1 
cv.destroyAllWindows()