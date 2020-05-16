import cv2 as cv
import numpy as np

img = cv.imread('filter_blur.jpg')

rx, ry = 12, 6  # half kernel
sx, sy = 6, 3  # spread of Gaussian in x and y direction

kernel = np.zeros((ry * 2+1, rx*2+1), np.float32)

for i in range(kernel.shape[0]):
    for j in range(kernel.shape[1]):
        x = j - rx  # x distance from the kernel center
        y = i - ry
        kernel[i, j] = np.exp(-(x**2) / (2*sx**2) - (y**2) / (2*sy**2))

cv.imshow('kernel', cv.resize(kernel, (400,200)))

# print('kernel sum = ', kernel.sum())
kernel /= kernel.sum() # make the kernel sum 1

img_smoothed = cv.filter2D(img, -1, kernel)

# rx*2+1, ry*2+1 is kernel size in x and y direction
img_blured = cv.GaussianBlur(img, (rx*2+1, ry*2+1), sigmaX=sx, sigmaY=sy)

# auto sigma from kernel size
img_blured1 = cv.GaussianBlur(img, (rx*2+1, ry*2+1), 0)

cv.imshow('original', img)
cv.imshow('smoothed', img_smoothed)
cv.imshow('blured', img_blured)
cv.waitKey()
