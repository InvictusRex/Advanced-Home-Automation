import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import time

try:
    ser = serial.Serial('COM6', 9600) 
    time.sleep(2)  
    print("Serial connection established.")
except serial.SerialException as e:
    print("Could not open serial port:", e)
    ser = None

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img) 

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print("Finger states:", fingers)
        finger_count = fingers.count(1)

        if ser:  
            if finger_count == 1:
                print("LIGHT ON")
                ser.write(b'5')  # Send '1' to Arduino
                time.sleep(0.1)  # Add a short delay for stability

            elif finger_count == 2:
                print("LIGHT OFF")
                ser.write(b'6')  # Send '2' to Arduino
                time.sleep(0.1)

            elif finger_count == 3:
                print("FAN ON")
                ser.write(b'7')  # Send '3' to Arduino
                time.sleep(0.1)

            elif finger_count == 4:
                print("FAN OFF")
                ser.write(b'8')  # Send '4' to Arduino
                time.sleep(0.1)

            elif finger_count == 5:
                print("ALL ON")
                ser.write(b'9')  # Send '5' to Arduino
                time.sleep(0.1)

    # Display the webcam feed
    cv2.imshow("Image", img)

    # Press 'q' to break the loop and exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

if ser:
    ser.close()  # Close the serial connection if it was opened
