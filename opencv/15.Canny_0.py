# Canny edge detector

import cv2 as cv

img = cv.imread('edge_test1.jpg')

# thresh2 가 thresh1보다 2~3 배정도 값이 권장됩니다.
thresh1, thresh2 = 50, 120

# thresh1과 thresh2 순서는 중요하지 않습니다.
edge = cv.Canny(img, thresh1, thresh2)

cv.imshow('img', img)
cv.imshow('edge', edge)
cv.waitKey()