##LEGSBY Mk.1 Program
##Ginger-Marie Wilkins
##UNLV EED Spring 2019

#import OpenCV and gpiozero
import cv2
import gpiozero as zero

#import only the sleep function from time
from time import sleep

#sets the haar-like features to be used. this file,
#along with others, is downloaded with OpenCV.  For
#best results, copy at minimum "Haarcascade_frontalface_default.xml"
#into the directory with the program in it, and rename it.
#here it is renamed "faces.xml"
face_cascade = cv2.CascadeClassifier('faces.xml')

#initializes the USB camera through OpenCV
cam = cv2.VideoCapture(0)

#counting variable, will be used in loop
cnt = 0

#for easy adjustment of the Pulse Width Modulation (PWM)
cor = 0.45
maxPW=(2.0+cor)/1000
minPW=(1.0-cor)/1000

#initializes the servo
servo = zero.Servo(17, min_pulse_width=minPW, max_pulse_width=maxPW)

#demonstrates that the servo is funcitoning, and
#initializes it at the front of the animatronic
servo.min()
sleep(1)
servo.max()
sleep(1)
servo.mid()
sleep(1)

servoNow = servo.value
##debug statements:
#print("servo.value")
#print(servoNow)
#servoNow = .5
#print("servoNow")
#print(servoNow)
#wid = 600

#infinite loop, which allows the camera to
#continuously feed images through the algorithm
#and trac to the face.
#significant lag to be expected
while(True):
    #allows for safe and clean exit of the infinite loop
    if cv2.waitKey(1) == 27: #escape key
        break
    else:
        #this is the fun stuff:
        
        #reads the camera to memory, flips it horizontally
        #and sets the dimenstions of the capture
        ret, imgBase = cam.read()
        img = cv2.flip(imgBase,1)
        ret = cam.set(cv2.CAP_PROP_FRAME_WIDTH,wid)
        ret = cam.set(cv2.CAP_PROP_FRAME_HEIGHT,wid)     
    
        #converts the camera to greyscale
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #begins detecting faces from the greyscale camera feed.
        #this must happen per frame taken, and so creates a good
        #deal of lag in the operation of the code.
        #face is an array with 4 values correstponding to the
        #location and dimenstion of the face found
        face = face_cascade.detectMultiScale(grey, 1.3, 10)
        
        #processes the coordinates of the face for varipous functions
        for (x,y,w,h) in face:
            #creates rectangle to be overlayed on the shown camera feed
            cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
#            roi_grey = grey[y:y+h, x:x+w]
#            roi_colr = img[y:y+h, x:x+w]

            #decided whether a defualt value should be used
            #or if the servo should try to follow the face.
            #there are flaws with the mathematical logic within
            #this, making the margin of motion too large and slow.
            if cnt >=1:
                #debugging statements
                print("presently at")
                print(servoNow)
                #moves ther servo and updates the servo location variable
                servo.value = float((x*0.001)-servoNow)-offset
                servoNow = servo.value
                #debugging statements
                print("moved to") 
                print(servoNow)
                print(x)
                sleep(1)
            else:
                #handles the initial loop
                offset = x*.001
                servoNow = offset
                cnt = cnt + 1
                #debugging stateents
                print("setting x")
                print(offset)
      
        #prints the camera in a window on the screen
        cv2.namedWindow("camera",cv2.WINDOW_AUTOSIZE)
        cv2.imshow("camera",img)        
        #prints the greyscale camera feed.  if desired, uncomment
#        cv2.namedWindow("grey", cv2.WINDOW_AUTOSIZE)
#        cv2.imshow("grey", grey)

#clean-up performed only upon safe exit of the infinite loop
cam.release()
cv2.destroyAllWindows()
servo.mid()

    


