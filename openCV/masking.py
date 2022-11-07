import cv2 as cv
import numpy as np

img=cv.imread('C:/Users/Praksa/cats/poodles.jpg')
cv.imshow('Dogs',img)

blank=np.zeros((300,300),dtype='uint8')#the dimensions of the mask MUST BE with same size as that of the image
cv.imshow('Blank Image',blank)

circle=cv.circle(blank.copy(),(img.shape[1]//2+45,img.shape[0]//2),100,255,-1)
#cv.imshow('Mask',mask)

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

weird_shape=cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape',weird_shape)

masked=cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shape Masked Image',masked)


cv.waitKey(0)