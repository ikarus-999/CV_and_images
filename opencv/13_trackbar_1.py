#multi trackbar

import cv2 as cv
import numpy as np

def onChangeBGR(self):
    val1 = cv.getTrackbarPos('B', 'img')
    val2 = cv.getTrackbarPos('G', 'img')
    val3 = cv.getTrackbarPos('R', 'img')
    img[:,:,0] = val1
    img[:,:,1] = val2
    img[:,:,2] = val3
    cv.imshow('img', img)

init_val = 128

img = np.full((480, 640, 3), init_val, np.uint8)

cv.namedWindow('img')
cv.createTrackbar('R', 'img', init_val, 255, onChangeBGR)
cv.createTrackbar('G', 'img', init_val, 255, onChangeBGR)
cv.createTrackbar('B', 'img', init_val, 255, onChangeBGR)

cv.imshow('img', img)
cv.waitKey()
