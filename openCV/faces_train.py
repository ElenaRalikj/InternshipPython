import os
import cv2 as cv
import numpy as np
#os.chdir('C:/Users/Praksa/cats/train')

#NE RABOTI!!!
#people=['Ben Affleck','Elton John','Jerry Seinfield', 'Madonna', 'Mindy Kaling']


people=[]

for i in os.listdir(r'C:\Users\Praksa\cats\train'):
    people.append(i)

print (people)


DIR=r'C:/Users/Praksa/cats/train'
#haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
haar_cascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
features=[]#image arrays of faces
labels=[]#corresponding labels

 # the function it's gonna loop through every folder and inside every folder it will loop through every image
#then it will grab the face in that image and add that to out training set
def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done--------------')
#first we need to convert this features and labels list to NumPy arrays

features=np.array(features,dtype='object')
labels=np.array(labels)

#print(f'Length of the features list={len(features)}')
#print(f'Length of the labels list={len(labels)}')

face_recognizer=cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the features list and the labels list

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
#first we need to convert this features and labels list to NumPy arrays

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)