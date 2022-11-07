import cv2 as cv
import numpy as np

img=cv.imread('C:/Users/Praksa/Downloads/Boston.jpg')

cv.imshow('Boston',img)


#Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])#a tuple of image width of 1 and image height of 0
    return cv.warpAffine(img,transMat,dimensions)

# -x--> left
# -y--> up
# x--> right
# y--> down

translated=translate(img,-100,100)
cv.imshow('Translated',translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
   # print(width)




    if rotPoint is None: #means that we are gonna rotate aroung the center
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) #1.0 is the scale
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow('Rotated',rotated)

rotated_rotated=rotate(img,-90)
cv.imshow('Rotated Rotated',rotated_rotated)


#Resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)#the interpolation
#(INTER_AREA for shrinking the image or stick with the default, INTER_LINEAR for enlarging the image,
# also INTER_CUBIC for enlargin an image but a little bit slower but with better quality
cv.imshow('Resized',resized)


#Flipping
flip=cv.flip(img,-1)
cv.imshow('Flip',flip)

#Cropping
cropped=img[200:400,300:400]
cv.imshow('Cropped',cropped)
#print(img.shape)


cv.waitKey(0)