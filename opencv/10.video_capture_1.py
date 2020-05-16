# play video file
import cv2 as cv

capture = cv.VideoCapture('capture.avi')
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv.CAP_PROP_FPS)
print('width, height =', width, height)
print('fps =', fps)

dt = int(1000./fps)

while True:
    ret, frame = capture.read()
    if ret:
        cv.imshow('frame', frame)
    else:
        break
    if cv.waitKey(dt) == 27: break

capture.release()