# Gesture Control
import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize the hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Detect hand and draw landmarks

    if hands:
        # Get the first hand detected
        hand = hands[0]
        
        # Get the state of each finger (1 for up, 0 for down)
        fingers = detector.fingersUp(hand)
        print("Finger states:", fingers)

        # Check for specific gestures
        if fingers == [0, 1, 1, 0, 0]:
            print("LIGHT ON")
            # Send command to hardware or perform action here

        elif fingers == [1, 1, 1, 1, 1]:
            print("LIGHT OFF")
            # Send command to hardware or perform action here

        elif fingers == [0, 1, 1, 1, 0]:
            print("FAN ON")
            # Send command to hardware or perform action here

        elif fingers == [1, 1, 0, 0, 0]:
            print("FAN OFF")
            # Send command to hardware or perform action here

    # Display the webcam feed
    cv2.imshow("Image", img)

    # Press 'q' to break the loop and exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
