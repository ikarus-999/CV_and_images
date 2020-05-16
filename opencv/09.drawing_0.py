import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

cv.line(img, (20,20), (620,460), (0,255,0), 3)

cv.rectangle(img, (100,100), (400,400), (0,0,255), 3)

cv.rectangle(img, (500,100), (600,200), (255,0,0), -1)

cv.circle(img, (320,240), 100, (255,255,0), 3)

cv.ellipse(img, (320,240), (300,200), 10, 0, 360, (0,255,255), 3)

pts = np.array([[50,150], [200,80], [350,120], [300,200]], np.int32)
cv.polylines(img, [pts.reshape((-1,1,2))], True, (255,0,255), 3)

pts = np.array([[350,350], [500,280], [630,320], [520,320]], np.int32)
cv.fillPoly(img, [pts.reshape((-1,1,2))], (0,0,255))

cv.putText(img, "Hello", (10,450),
           cv.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 3)

cv.imshow('img', img)
cv.waitKey()