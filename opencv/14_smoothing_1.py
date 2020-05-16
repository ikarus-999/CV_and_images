import cv2 as cv
import numpy as np

init_val = 1

def skew_sigma(self):
    x = max(cv.getTrackbarPos('sigma_x', 'smooth'), 0.01)
    y = max(cv.getTrackbarPos('sigma_y', 'smooth'), 0.01)
    smoothed = cv.GaussianBlur(img, (0, 0), sigmaX=x, sigmaY=y)
    cv.imshow('smooth', smoothed)

img = cv.imread('filter_blur.jpg')

sigma_x, sigma_y = 3, 3

smoothed = cv.GaussianBlur(img, (0,0), sigmaX=sigma_x, sigmaY=sigma_y)
cv.namedWindow('smooth')
cv.createTrackbar('sigma_x', 'smooth', init_val, 10, skew_sigma)
cv.createTrackbar('sigma_y', 'smooth', init_val, 10, skew_sigma)
cv.imshow('smooth', img)
cv.waitKey()