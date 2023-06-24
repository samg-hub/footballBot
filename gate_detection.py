import cv2 as cv
import imutils
import numpy as np
from copy import deepcopy

def find_ball(frame, uHSV, lHSV, erode, dilate):
    foundcenter = ...
    frame = imutils.resize(frame , width=600)
    blurred = cv.GaussianBlur(frame ,(11,11) ,0)
    hsv = cv.cvtColor(blurred , cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lHSV, uHSV)
    mask = cv.erode(mask, None, iterations = erode)
    mask = cv.dilate(mask, None, iterations = dilate)
    contours = cv.findContours(deepcopy(mask), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if len(contours) > 0 :
        c = max(contours , key=cv.contourArea)
        rect = cv.minAreaRect(c)
        foundcenter = rect[0]
    return foundcenter