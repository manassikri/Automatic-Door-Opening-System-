import cv2
import RPi.GPIO as GPIO
import time

cam = cv2.VideoCapture(0)
cam.set(3, 200)
cam.set(4,200)

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
while True:

    ret_val,img=cam.read(1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th =50.0


    faces = face_cascade.detectMultiScale(gray, 1.1, 12)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        if (w*h > th):
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(38,GPIO.OUT)
            GPIO.setup(40,GPIO.OUT)
            GPIO.output(38,GPIO.HIGH)
            GPIO.output(40,GPIO.LOW)
            print('1')
            time.sleep(8)
            GPIO.cleanup()

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(38,GPIO.OUT)
            GPIO.setup(40,GPIO.OUT)
            GPIO.output(40,GPIO.HIGH)
            GPIO.output(38,GPIO.LOW)
            print('2')
            time.sleep(8)
            GPIO.cleanup()



    cv2.imshow('output',img)






    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
