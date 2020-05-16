import cv2 as cv
import numpy as np

def on_ep_change(_):
    sigma_s = cv.getTrackbarPos('sigma_s', 'edge_preserved')
    sigma_r = cv.getTrackbarPos('sigma_r', 'edge_preserved') * 0.01
    print('edge_preserved : sigma_s, sigma_r = ', sigma_s, sigma_r)
    dst = cv.edgePreservingFilter(img, sigma_s=sigma_s, sigma_r=sigma_r)
    cv.imshow('edge_preserved', dst)

def on_detail_change(_):
    sigma_s_det = cv.getTrackbarPos('sigma_s_detail', 'detail')
    sigma_r_det = cv.getTrackbarPos('sigma_r_detail', 'detail') * 0.01
    dst = cv.detailEnhance(img, sigma_s=sigma_s_det, sigma_r=sigma_r_det)
    cv.imshow('detail', dst)

def on_pencil_change(_):
    sigma_s = cv.getTrackbarPos('sigma_s_pencil', 'pencil')
    sigma_r = cv.getTrackbarPos('sigma_r_pencil', 'pencil') * 0.01
    dst_gray, dst_color  = cv.pencilSketch(img, sigma_s=sigma_s, sigma_r=sigma_r)
    cv.imshow('pencil_gray', dst_gray)
    cv.imshow('pencil', dst_color)

def on_style_change(_):
    sigma_s = cv.getTrackbarPos('sigma_s', 'style')
    sigma_r = cv.getTrackbarPos('sigma_r', 'style') * 0.01
    dst = cv.stylization(img, sigma_s=sigma_s, sigma_r=sigma_r)
    cv.imshow('style', dst)

img = cv.imread('red-and-green-leavs-of-autumn-jpg.jpg')

cv.namedWindow('edge_preserved')
cv.createTrackbar('sigma_s', 'edge_preserved', 60, 60, on_ep_change)
cv.createTrackbar('sigma_r', 'edge_preserved', 40, 100, on_ep_change)

cv.namedWindow('detail')
cv.createTrackbar('sigma_s_detail', 'detail', 60, 60, on_detail_change)
cv.createTrackbar('sigma_r_detail', 'detail', 40, 100, on_detail_change)

cv.namedWindow('pencil')
cv.createTrackbar('sigma_s_pencil', 'pencil', 60, 60, on_pencil_change)
cv.createTrackbar('sigma_r_pencil', 'pencil', 20, 100, on_pencil_change)

cv.namedWindow('style')
cv.createTrackbar('sigma_s', 'style', 60, 60, on_style_change)
cv.createTrackbar('sigma_r', 'style', 45, 100, on_style_change)

cv.imshow('img', img)

on_ep_change(0)
on_detail_change(0)
on_pencil_change(0)
on_style_change(0)

cv.waitKey()
