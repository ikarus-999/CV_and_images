from builtins import tuple

import cv2 as cv
import numpy as np

img0 = cv.imread('optical-flow0.png')
img1 = cv.imread('optical-flow1.png')

cv.imshow('img0', img0)
cv.imshow('img1', img1)

img0_gray = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)
img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

feature_params = dict(maxCorners=100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize=7)

pts0 = cv.goodFeaturesToTrack(img0_gray, **feature_params)
print('pts0: ', pts0.shape, pts0.dtype)

lk_params = dict(winSize = (15,15),
                 maxLevel = 5,
                 criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

pts1, status, error = cv.calcOpticalFlowPyrLK(img0_gray, img1_gray, pts0, None, **lk_params)

print('pts1: ', pts1.shape, pts1.dtype)


pts0_success = pts0[status==1]
pts1_success = pts1[status==1]

print('p0_success: ', pts0_success.shape)
print('p1_success: ', pts1_success.shape)

for p in pts0_success:
    cv.circle(img0, tuple(p), 3, (0, 0, 255))

for p in pts1_success:
    cv.circle(img1, tuple(p), 3, (0, 255, 0))

cv.imshow('img0', img0)
cv.imshow('img1', img1)
cv.waitKey()
