# mode 1:line, 2:rectangle, 3:circle, 4:free
import cv2 as cv
import numpy as np

x0, y0 = 0, 0
draw = False
mode = 1
img0 = np.zeros((480,640,3), np.uint8)
img = np.copy(img0)

def on_mouse(event, x, y, flags, param):
    global x0, y0, draw, img0, img

    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
        x0, y0 = x, y
    elif draw and event == cv.EVENT_MOUSEMOVE:
        if mode < 4: np.copyto(img, img0)
        if mode == 1:
            cv.line(img, (x0,y0), (x,y), (0,0,255), 2)
        elif mode == 2:
            cv.rectangle(img, (x0,y0), (x,y), (0,255,0), 2)
        elif mode == 3:
            r = np.sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
            cv.circle(img, (x0,y0), int(r), (0,255,255), 2)
        elif mode == 4:
            cv.line(img, (x0,y0), (x,y), (255,0,255), 2)
            x0, y0 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        np.copyto(img0, img)
        draw = False


cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse)

while True:
    cv.imshow('img', img)
    key = cv.waitKey(30)
    if key > 48 and key < 53: mode = key-48
    if key == 27: break