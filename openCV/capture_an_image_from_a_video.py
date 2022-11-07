import cv2 as cv
import os

capture=cv.VideoCapture('C:/Users/Praksa/Downloads/pexels-yan-5478927.mp4')


def rescaleFrame(frame,scale=0.75):
    #Images, Videos and Live Video
    width=int(frame.shape[1]*scale)
    height =int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#Reading the video frame by frame

while True:
    isTrue, frame = capture.read()

    frame_resized=rescaleFrame(frame,scale=0.2)

    cv.imshow('Video',frame) #display an individual frame
    cv.imshow('Video Resized',frame_resized)
    cv.imwrite('Frame1.jpg',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #stopping the video from playing indefinitely; if the letter d is pressed then break out of this loop and stop displaying the video
        break


def rescaleFrame(frame,scale=0.75):
    #Images, Videos and Live Video
    width=int(frame.shape[1]*scale)
    height =int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture.release()
cv.destroyAllWindows()
