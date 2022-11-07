import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#img=cv.imread('C:/Users/Praksa/cats/sign111.jpg')
#cv.imshow('Stop',img)

#print(img.shape)


#blank=np.zeros(img.shape,dtype='uint8')
#cv.imshow('Blank',blank)

#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#canny=cv.Canny(blur,125,175)
#cv.imshow('Canny Edges',canny)

#contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#print(f'{len(contours)} contour(s) found!')

#cv.drawContours(blank,contours,-1,(0,0,255),1)
#cv.imshow('Contours Drawn',blank)

#Template matching( Object Detection)

img=cv.imread('C:/Users/Praksa/cats/limitspeedontheroad40.jpg',0)
#directly resizing it img=cv.resize(cv.imread('path',0),(0,0),fx=0.8,fy=0.8)
#so it means that we need to resize the template image too template=cv.resize(cv.imread('path',0),(0,0),fx=0.8,fy=0.8)
template=cv.imread('C:/Users/Praksa/cats/limitsigncropped.jpg',0)
h,w=template.shape
#(heigh,width,instead having 3 channels we only have one integer value between 0 and 255 representing each of our pixels)
print(img)

methods=[cv.TM_CCOEFF,cv.TM_CCOEFF_NORMED,cv.TM_CCORR,
         cv.TM_CCORR_NORMED,cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]#all of the different methods for doing template matching

for method in methods:
    img2=img.copy()

    result=cv.matchTemplate(img2,template,method)
    #performing a convolution (taking the template image and kind of sliding it around our base image and seeing how close of a match there is in every single region of our base image
    #the result will return a ''new image'', actually a two dimensional array that will tell us roughly how accurate of a match there is in each region of our image
    #(W-w+1,H-h+1) #the upper case W is the width of our base image so the lower case w is going to be the width of the template image
    #+1 stands for one position
    min_val,max_val,min_loc,max_loc= cv.minMaxLoc(result)
    print('Location of the minimum value=',min_loc,'Location of the maximum value=',max_loc)
    if method in[cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location=max_loc

    bottom_right=(location[0]+w,location[1]+h)
    cv.rectangle(img2,location,bottom_right,255,5)
    cv.imshow('Match',img2)
    cv.waitKey(0)
    cv.destroyAllWindows()




#(4-2+1,4-2+1)=(3,3)#3 by 3 is the number of  times we can slide this image in the x direction and in the y direction
#W=4
#w=2
#H=4
#h=2
#4x4
#2x2

#[[255,255,255,255],
# [255,255,255,255],
# [255,255,255,255],
# [255,255,255,255]]

#[[255,255],
# [255,255]]

#[[0,0,0],
 #[0,1,0],
 #[0,0,0]]  #by looking at this output array we are trying to figure out which value is the highest or which value is the lowest
            #actually it's telling us which areas match the most and which areas match the least amount