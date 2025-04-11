# Home Automation System using Gesture Control, Speech Recognition & Mobile App Interface
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Arduino](https://img.shields.io/badge/Arduino-Compatible-teal.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Overview

This project is an advanced home automation system that combines **real-time Gesture Control**, **Speech Recognition**, and a **Mobile App Interface** to provide a seamless, touchless smart home experience. Users can control home appliances like lights and fans using hand gestures, voice commands, or a remote mobile app developed using **MIT App Inventor**. The system is designed for convenience, accessibility, and hygiene.

## 🌟 Key Features

### 1. Real-Time Gesture Recognition
- Utilizes **OpenCV** and **CVZone HandTrackingModule** for real-time hand tracking and gesture recognition.
- Tracks up to **21 key hand landmarks** with high accuracy and confidence.
- Detects both single and dual-hand gestures.

### 2. Speech Recognition
- Integrated with **Google Speech-to-Text API** for real-time speech command recognition.
- Supports natural language commands like:
  - "Turn on the light."
  - "Switch off the fan."
  - "Turn off all appliances."

### 3. Mobile App Interface
- A user-friendly mobile app developed using **MIT App Inventor**.
- Allows remote control of appliances via touch or voice commands.
- Provides real-time synchronization with the hardware system.

### 4. Multi-Device Control
- Control multiple appliances, including:
  - Lights (ON/OFF).
  - Fans (ON/OFF).
  - All appliances at once.

### 5. Flexible Control Methods
- **Gesture-Based Control**:
  - 1 finger → Light ON
  - 2 fingers → Light OFF
  - 3 fingers → Fan ON
  - 4 fingers → Fan OFF
  - 5 fingers → ALL ON
- **Speech-Based Control**:
  - Commands processed via the Google Speech-to-Text API.
- **Mobile App Control**:
  - Control appliances remotely using the app.

### 6. Arduino Integration
- Communicates with Arduino via serial communication for hardware control.
- Supports both numeric and text-based command protocols.

### 7. User-Friendly Feedback
- Provides visual feedback on gesture detection through the webcam feed.
- Logs speech and gesture commands in the console for debugging.

## 🔧 Technical Architecture

### Hardware Requirements
- Webcam for gesture detection.
- Microphone for speech recognition.
- Arduino board for hardware communication.
- Relay modules to control appliances.
- Smartphone or tablet for the mobile app.
- Home appliances for testing.

### Software Components
- **Python 3.x**: Main programming language for the system.
- **OpenCV**: For image processing and gesture recognition.
- **CVZone**: For hand tracking and landmark detection.
- **PySerial**: For serial communication with Arduino.
- **Google Speech-to-Text API**: For real-time speech recognition.
- **MIT App Inventor**: For building the mobile app interface.

## 📁 Repository Structure

```
Home-Automation/
├── hands_control.py                     # Basic gesture recognition implementation
├── final_code_with_MIT_app.py          # Advanced implementation with Arduino integration
├── Gesture Control_arduino_compatible.py # Arduino-compatible implementation
├── Mobile_App_Interface/                # Source code for the mobile app
├── speech_recognition_integration.py   # Speech recognition implementation
├── Project Report_Home Automation_MPMC.pdf # Detailed project report
└── README.md                            # Project documentation
```

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
3. Connect relay modules to the Arduino for controlling appliances.

### Step 4: Set Up Mobile App
1. Navigate to the `Mobile_App_Interface/` directory.
2. Import the MIT App Inventor project file into **MIT App Inventor**.
3. Customize the app with your Arduino's serial connection details.
4. Deploy the app on your smartphone or tablet.

### Step 5: Run the System
Choose the desired implementation and run the corresponding script:
```bash
python hands_control.py                     # For basic gesture recognition
python final_code_with_MIT_app.py          # For advanced implementation
python speech_recognition_integration.py   # For speech recognition
```

### Step 6: Test the System
1. Ensure the webcam is properly positioned for gesture detection.
2. Use the mobile app or voice commands to control the appliances.
3. Check the console for logs and feedback.

## 💡 Advantages

1. **Touchless Control**:
   - Promotes hygiene by eliminating the need for physical switches.
   - Ideal for accessibility and modern smart homes.

2. **User-Friendly Experience**:
   - Intuitive gesture recognition.
   - Natural language speech commands.
   - Remote control via a mobile app.

3. **Flexibility**:
   - Multiple control methods to suit user preferences.
   - Easily extendable for additional appliances.

4. **Scalability**:
   - Compatible with other IoT devices and systems.
   - Future-proof architecture for adding more features.

## 🎯 Future Enhancements

- [ ] Add a web-based control interface.
- [ ] Integrate machine learning for more complex gesture recognition.
- [ ] Enhance speech recognition with advanced NLP capabilities.
- [ ] Add support for more home appliances.

## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
