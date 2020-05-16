# draw rectangles
import cv2 as cv
import numpy as np

x0, y0 = 0, 0
draw = False
img0 = np.zeros((480,640,3), np.uint8)
img = np.copy(img0)

def on_mouse(event, x, y, flags, param):
    global x0, y0, img0, img, draw

    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
        x0, y0 = x, y
    elif draw and event == cv.EVENT_MOUSEMOVE:
        np.copyto(img, img0)
        cv.rectangle(img, (x0,y0), (x,y), (0,255,0), 2)
    elif event == cv.EVENT_LBUTTONUP:
        np.copyto(img0, img)
        draw = False

cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse)

while True:
    cv.imshow('img', img)
    key = cv.waitKey(30)
    if key == 27: break