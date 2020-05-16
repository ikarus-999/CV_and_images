import cv2 as cv
import numpy as np


def onChange():
    red = cv.getTrackbarPos('R', 'img')
    green = cv.getTrackbarPos('G', 'img')
    blue = cv.getTrackbarPos('B', 'img')

    img.fill(red, green, blue)
    cv.imshow('img', img)

init_val = 128
img = np.full((480, 640), init_val, np.uint8)
cv.namedWindow('img')
cv.createTrackbar('R', 'img', init_val, 255, onChange)
cv.createTrackbar('G', 'img', init_val, 255, onChange)
cv.createTrackbar('B', 'img', init_val, 255, onChange)



cv.imshow('img', img)
cv.waitKey()
