import cv2 as cv

capture = cv.VideoCapture(0)
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv.CAP_PROP_FPS)
print('width, height =', width, height)
print('fps =', fps)

#fourcc = cv.VideoWriter_fourcc(*'XVID')
fourcc = cv.VideoWriter_fourcc(*'MPEG')
writer = cv.VideoWriter('capture.avi', fourcc,
                        fps, (width,height))

while True:
    ret, frame = capture.read()
    writer.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27: break

capture.release()
writer.release()