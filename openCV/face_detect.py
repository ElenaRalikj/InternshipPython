import cv2 as cv

#img=cv.imread('C:/Users/Praksa/cats/people.jpg')
#img=cv.imread('C:/Users/Praksa/cats/people1.jpg')
#img=cv.imread('C:/Users/Praksa/cats/people2.png')
#img=cv.imread('C:/Users/Praksa/cats/people3.jpg') #not detecting some of the faces, it is expected because haar cascades are sensitive to noise in an image
img=cv.imread('C:/Users/Praksa/cats/people4.jpg')
#possible solution:minimizing the sensitivity to noise by modifying the scale factor in minimum neighbors
#by minimizing the minNeighbors value, we are making the haar cascades more prone to noise
cv.imshow('Group of 8 people',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)#we dont need any color in the image cause
#the haarcascades look at an object in an image amd using the edges tries to
#determine whether it's a face or not


#haar_cascade=cv.CascadeClassifier(r'C:\Users\Praksa\PycharmProjects\pythonProject\haar_face.xml')
#haar_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

print("HE HE HE ")
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)

print("LE LE zasp nejke")
cv.imshow('Gray Person',gray)
print("Number of faces found =" ,len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces',img)


cv.waitKey(0)
