import cv2

face_cascade = cv2.CascadeClassifier('faces.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')

cam = cv2.VideoCapture(0)

while(True):
    if cv2.waitKey(1) == 27:
        break
    else:

        tf, img = cam.read()
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     
        
        face = face_cascade.detectMultiScale(grey, 1.3, 10)
        
        for (x,y,w,h) in face:
            print("x,y,w,h")
            print(x)
            print(y)
            print(w)
            print(h)
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
            roi_grey = grey[y:y+h, x:x+w]
            roi_colr = img[y:y+h, x:x+w]
            
           
            eye = eye_cascade.detectMultiScale(roi_grey, 1.3, 5)
            for (ex,ey,ew,eh) in eye:
                
#                print("eye: x,y,w,h")
#                print(ex)
#                print(ey)
#                print(ew)
#                print(eh)
                
                cv2.rectangle(roi_colr,(ex,ey),(ey+ew,ey+eh), (0,255,0),2)
#                print("per loop")
       
        cv2.namedWindow("camera",cv2.WINDOW_AUTOSIZE)
        cv2.imshow("camera",img)        
        
#        cv2.namedWindow("grey", cv2.WINDOW_AUTOSIZE)
#        cv2.imshow("grey", grey)
#cam.release()
cv2.destroyAllWindows()
    
