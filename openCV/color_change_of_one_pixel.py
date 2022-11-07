import cv2 as cv
import numpy as np

blank=cv.imread('C:/Users/Praksa/Downloads/Boston.jpg')

cv.imshow('Boston',blank)

rgb=cv.cvtColor(blank,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#blank[200:300,300:400]=0,0,255
#cv.imshow('Red',blank)

#blank = np.zeros((600,420,3), dtype='uint8')
#cv.imshow('Blank Image',blank)

print(rgb.shape)

rgb[200:220,320:340]=[0,0,255]

cv.imshow('Changed pixel',rgb)

cv.waitKey(0)
