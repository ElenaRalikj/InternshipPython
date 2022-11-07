import cv2 as cv

img = cv.imread('C:/Users/Praksa/cats/cats2.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale=0.75):
    #Images, Videos and Live Video
    width=int(frame.shape[1]*scale)
    height =int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Only works for live Video
    capture.set(3,width)
    capture.set(4,height)
    capture.set

#resized_image=rescaleFrame(img,scale=.2)
#cv.imshow('Image', resized_image)
# Reading Videos

capture=cv.VideoCapture('C:/Users/Praksa/Downloads/pexels-yan-5478927.mp4')#this is an instance of the video capture clause

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=.2)

    cv.imshow('Video',frame) #display an individual frame
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #stopping the video from playing indefinitely; if the letter d is pressed then break out of this loop and stop displaying the video
        break

capture.release() #we release the capture device
cv.destroyAllWindows()


