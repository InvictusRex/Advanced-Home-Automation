#Gesture Control
import cv2 
import cvzone
from cvzone.HandTrackingModule import HandDetector
import serial
import time
# arduino = serial.Serial('COM7', 9600)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        print(fingers1)
        if(fingers1[0]==0) & (fingers1[1]==1) & (fingers1[2]==1) & (fingers1[3]==0) & (fingers1[4]==0) :
            print("LIGHT ON")
            value="dog"
            value=value+'\r'
            # arduino.write(value.encode())
        if(fingers1[0]==1) & (fingers1[1]==1) & (fingers1[2]==1) & (fingers1[3]==1) & (fingers1[4]==1):
            print("LIGHT OFF")
            value="cat"
            value=value+'\r'
            # arduino.write(value.encode())
        if(fingers1[0]==0) & (fingers1[1]==1) & (fingers1[2]==1) & (fingers1[3]==1) & (fingers1[4]==0) :
            print("FAN ON")
            value="bat"
            value=value+'\r'
            # arduino.write(value.encode())
        if(fingers1[0]==1) & (fingers1[1]==1) & (fingers1[2]==0) & (fingers1[3]==0) & (fingers1[4]==0):
            print("FAN OFF")
            value="rat"
            value=value+'\r'
            # arduino.write(value.encode())
    
        #ser.sendData()
    cv2.imshow("Image", img)
    cv2.waitKey(1)