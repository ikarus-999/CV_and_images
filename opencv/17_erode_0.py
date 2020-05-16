import cv2 as cv
import numpy as np

mat = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 8, 7],
                [6, 5, 4, 3]], np.uint8)

print(mat)
print('==' * 10)
# 침식
kernel = np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]], np.uint8)

eroded = cv.erode(mat, kernel)
print('eroded')
print(eroded)