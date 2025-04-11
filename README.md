# Home Automation using Gesture Control, Speech Recognition, & Mobile App Interface 🏠✨
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Arduino](https://img.shields.io/badge/Arduino-Compatible-teal.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Overview

This project presents an innovative approach to home automation by combining **gesture control**, **speech recognition**, and a **mobile app interface**. By leveraging computer vision and natural language processing (NLP), the system enables touchless control of home appliances such as lights and fans. The mobile app further extends the system's accessibility and allows users to control appliances remotely using speech commands.

## 🌟 Key Features

### 1. Real-Time Gesture Recognition
- Utilizes OpenCV and CVZone's HandTrackingModule for accurate hand detection.
- Tracks up to 21 key hand landmarks in real time.
- Detects single or dual hands with a confidence threshold of 80%.

### 2. Multi-Device Control
- Control multiple appliances and devices:
  - Turn lights ON/OFF.
  - Turn fans ON/OFF.
  - Control all devices simultaneously.
- Support for both gesture-based and speech-based control.

### 3. Flexible Gesture Control
- **Finger Count-Based Control**:
  - 1 finger → Light ON
  - 2 fingers → Light OFF
  - 3 fingers → Fan ON
  - 4 fingers → Fan OFF
  - 5 fingers → ALL ON
- **Specific Gesture-Based Control**:
  - Peace sign (✌️) → Light ON
  - All fingers up (🖐️) → Light OFF
  - Three middle fingers up → Fan ON
  - Thumb + Index → Fan OFF

### 4. Speech Recognition
- Integrated with Google Speech-to-Text API for real-time speech recognition.
- Enables hands-free operation by understanding user commands such as:
  - "Turn on the light."
  - "Switch off the fan."
  - "Turn off all appliances."
- Supports natural language variations for enhanced usability.

### 5. Mobile App Interface (MIT App)
- Provides a seamless user interface for remote control of appliances.
- Speech commands can be issued through the mobile app.
- Gesture-based control can be visualized on the mobile app.
- Real-time synchronization with the Arduino hardware.

### 6. Arduino Integration
- Communicates with Arduino via serial communication for hardware control.
- Supports both numeric and text-based command protocols.

### 7. User-Friendly Interface
- Provides visual feedback on detected gestures via a webcam feed.
- Simple console logs for debugging and monitoring.

## 🔧 Technical Architecture

### Hardware Requirements
- Webcam for gesture detection.
- Microphone for speech recognition.
- Arduino board for hardware communication.
- Relay modules to control appliances.
- Smartphone or tablet for accessing the mobile app.
- Home appliances for testing.

### Software Components
- **Python 3.x**: Main programming language.
- **OpenCV**: For image processing and video feed handling.
- **CVZone**: For hand tracking and gesture recognition.
- **PySerial**: For serial communication with Arduino.
- **Google Speech-to-Text API**: For speech recognition.
- **MIT App Inventor**: For building the mobile app interface.

### Communication Protocols
- **Serial Communication**:
  - Default Port: COM6
  - Baud Rate: 9600
- **Command Formats**:
  - Numeric (e.g., 5 for Light ON).
  - Text-based (e.g., "dog" for Light ON).

## 📁 Repository Structure

```
Home-Automation/
├── hands_control.py                     # Basic gesture recognition implementation
├── final_code_with_MIT_app.py          # Advanced implementation with Arduino integration
├── Gesture Control_arduino_compatible.py # Arduino-compatible implementation
├── Mobile_App_Interface/                # Source code for the mobile app
├── Project Report_Home Automation_MPMC.pdf # Detailed project report
└── README.md                            # Project documentation
```

## 🚀 Implementation Details

### 1. `hands_control.py`
- **Purpose**: A basic implementation for gesture recognition using a webcam.
- **Key Features**:
  - Single-hand tracking with 80% confidence.
  - Visual feedback for gesture detection.
  - Console output for gesture states (e.g., "LIGHT ON").

### 2. `final_code_with_MIT_app.py`
- **Purpose**: A production-ready implementation with Arduino integration.
- **Key Features**:
  - Serial communication for hardware control.
  - Finger count-based gesture recognition.
  - Error handling for serial port issues.
  - Sends numeric commands to Arduino for appliance control.

### 3. `Gesture Control_arduino_compatible.py`
- **Purpose**: An Arduino-compatible implementation with extended features.
- **Key Features**:
  - Dual-hand tracking.
  - Advanced hand data (e.g., landmarks, bounding boxes).
  - Text-based command protocol for hardware control.

### 4. Mobile App Interface
- **Purpose**: Extends functionality to smartphones and tablets.
- **Key Features**:
  - Speech command support via Google Speech-to-Text API.
  - Real-time appliance control through a user-friendly UI.
  - Synchronization with Arduino for gesture and speech commands.

## 🛠️ Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/ZhadowNyx/Home-Automation.git
cd Home-Automation
```

### Step 2: Install Dependencies
Install the required Python packages:
```bash
pip install opencv-python cvzone pyserial google-api-python-client
```

### Step 3: Configure Arduino
1. Connect your Arduino board to the system.
2. Upload the appropriate sketch to the Arduino.
3. Connect relay modules to the Arduino for appliance control.

### Step 4: Set Up Mobile App
1. Import the MIT App Inventor project file from `Mobile_App_Interface/`.
2. Customize the app with your Arduino's serial connection details.
3. Deploy the app on your smartphone or tablet.

### Step 5: Run the Code
Choose the desired implementation and run the corresponding script:
```bash
python hands_control.py                     # For basic gesture recognition
python final_code_with_MIT_app.py          # For advanced implementation
python "Gesture Control_arduino_compatible.py" # For Arduino compatibility
```

### Step 6: Test the System
1. Align the webcam for gesture detection.
2. Use the mobile app to issue speech commands.
3. Monitor the console for feedback and debug logs.

## 💡 Novelty and Advantages

1. **Touchless Operation**:
   - Promotes hygiene by reducing surface contact.
   - Ideal for accessibility and smart home environments.

2. **Speech Recognition**:
   - Enhances convenience for users who prefer verbal commands.
   - Supports natural language variations for flexibility.

3. **Mobile App Integration**:
   - Provides a seamless remote control interface.
   - Allows users to issue commands from anywhere in the house.

4. **Scalability**:
   - Easily extendable for additional devices.
   - Compatible with other IoT technologies.

## 🎯 Future Enhancements

- [ ] Add more natural language processing capabilities.
- [ ] Integrate machine learning for gesture prediction.
- [ ] Add support for additional appliances.
- [ ] Develop a web-based control interface.

## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
