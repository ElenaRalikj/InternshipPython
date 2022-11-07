import cv2 as cv

img=cv.imread('C:/Users/Praksa/cats/catss.jpg')
cv.imshow('Cats',img)

#What happens when applying blur:
#Firstly we are defining a kernel/window, actually it's the window that we are drawing it over
#an image, so essentially it's a window that we draw over a specific portion of an image
#and sth happens on the pixels in this window
#so essentially this window has a size, a size that is called a kernel size
#Kernel size is basically the number of rows and the number of columns
#ex.Having 3 rows, 2 columns, the kernel size is 3x3
#We have multiple methods to apply some blur, essentially blur is applied to the middle pixel
#as a result of the pixels around it, also called the surrounding pixels

#Averaging-first method of blurring, we define a kernel window over a specific
#portion of an image, this window will essentially compute the pixel intensity of
#the middle pixel of the true center as the average of the surrounding pixel intensities
#ex.1 8 4
#   6 _ 5
#   3 7 2
#essentially the new pixel intensity for the centar region will be the average
#of all surrounding pixel intensity; so that's summing up all the numbers/8
#8 is the number of surrounding pixels
#we use that result as the pixel intensity for the middle value or the true center
#this process happens throughout the image so it computes all the pixels in the image


average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)
#higher kernel size we specify, the more blur there is

#Gaussian Blur
# does the same thing as averaging except that instead of computing the average of all of
#this running pixel intensity, each running pixel is given a particular weight
#and essentially the average of the products of those weights gives us the value
#for the true center
#using this method, we tend to get less blurring than compared to the averaging method
#however, the Gaussian Blur is more natural as compared to averaging

gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussinan Blur',gauss)
#less blurred than the average blur, it s because it was added a certain
#weight value when computing the blur

#Median Blur
#same thing as averaging except that instead of finding the average
#of the surrounding pixels, if finds the median of the surrounding pixels
#MEdian blurring tends  to be more effective in reducing noise in an image as
#compared to averaging and even Gaussian blur

median=cv.medianBlur(img,3) #here it s not a tuple of 3 by 3 but only an integer
#reason=openCV automatically assumes that this kernel size will be a 3 by 3 just based of this integer
cv.imshow('Median Blur',median)
#in general median blurring is not meant for high kernel sizes like 7 or even 5
#in some cases and it's more effective in reducing some of the noise in the image

#Bilateral Blur
#the most effective; used in a lot of advanced computer vision projects because of how it blurs
#all the other methods blur the image without looking at whether you are
#reducing edges in the image or not
#bilateral blur on the other side applies blurring but retains the edges in the image
bilateral=cv.bilateralFilter(img,10,35,25)
#the second element is a diameter not a kernel
cv.imshow('Bilateral Blur',bilateral)
#higher values of space sigma for bilateral blurring
#kernel size for mediam blurring
#both end up with a washed up, smudged version of this image

cv.waitKey(0)