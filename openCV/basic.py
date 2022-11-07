import cv2 as cv

img=cv.imread('C:/Users/Praksa/Downloads/Boston.jpg')

cv.imshow('Boston',img)

#Converting an Image to grayscale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur an Image

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)



#Edge Cascade

canny=cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilatin the Image
dilated=cv.dilate(canny,(7,7), iterations=3)
cv.imshow('Dilated',dilated)

#Eroding
eroded=cv.erode(dilated,(7,7), iterations=3)#getting the edges back
cv.imshow('Eroded',eroded)

#Resize

resize=cv.resize(img,(500,500) ,interpolation=cv.INTER_CUBIC)#ignoring the ascpect ratio
#in some cases if we are trying to enlarge the image and scale the image to a much larger dimensions we need to use
#the INTER_LINEAR or the INTER_CUBIC->the slowest among them all, but the resulting image is with much higher quality than the
#INTER_AREA or the INTER_LINEAR

#Cropping
cropped=img[50:200,200:400] #array slicing
cv.imshow('Cropped',cropped)


cv.imshow('Resized',resize)

cv.waitKey(0)