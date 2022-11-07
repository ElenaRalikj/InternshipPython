import cv2 as cv


img=cv.imread('C:/Users/Praksa/cats/poodles.jpg')
cv.imshow('Dogs',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

#Simple Thresholding
threshold,thresh=cv.threshold(gray,150, 255,cv.THRESH_BINARY) #it will check the whole image
#if the pixel value is greater than 150 it will set it to white(255)
#thresh is the binarized image; threshold is 150 which we have set
cv.imshow('Simple Thresholded',thresh)

#Inverse Threshold image
threshold,thresh_inv=cv.threshold(gray,150, 255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Invers',thresh_inv)

#Adaptive Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11, 9)
cv.imshow('Adaptive Thresholding',adaptive_thresh)
cv.waitKey(0)