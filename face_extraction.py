import numpy as np
import cv2
import os
import time


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:/Users/HP/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')


i=0
j=0

print("Enter name of class:")
name=raw_input()
os.mkdir(name) 

print("Enter number of minutes for class:")
number_of_minutes=int(raw_input())

print("Enter the number of minutes for break between images:")
minutes_break=int(raw_input())

print("Enter maximum number of faces to be extracted from image:")
number_of_faces=int(raw_input())

number_of_loops=int(number_of_minutes/minutes_break)
f= open(name+"/"+name+".txt","w+")

while True:

    img = cv2.imread('sachin.jpg')
    #ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3 , 5)
        
    
    for (x,y,w,h) in faces:
        

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
        crimg = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
        crimg = cv2.cvtColor(crimg, cv2.COLOR_BGR2GRAY) #transform to gray scale
        cv2.resize(crimg, (48, 48)) #resize to 48x48

        path = 'C:/Users/HP/Desktop/PROJECT/'+name
        cv2.imwrite(os.path.join(path , str(j)+"."+str(i)+".jpg"),crimg)

        i=i+1
        
        if((i==number_of_faces) or (i==len(faces))):
            break;


    cv2.imwrite(os.path.join('C:/Users/HP/Desktop/PROJECT/'+name+'/' , "image"+str(j)+".jpg"),img)

    f.write("%d\r\n" % (i))


        
        
    j=j+1
    i=0
    if(number_of_loops== j ):
        break;

    

    time.sleep(minutes_break*60) # Delay for 1 minute (60 seconds).

f.close()
cap.release()
