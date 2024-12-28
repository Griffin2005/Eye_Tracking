# Eye Controlled Mouse System

This project implements an **Eye Controlled Mouse System** using **OpenCV**, **MediaPipe**, and **PyAutoGUI**. The system allows users to control the 
mouse pointer and perform clicks based on eye movements, making it a valuable assistive tool for individuals with disabilities.

---

## Features

- **Real-Time Eye Tracking**:
  - Tracks eye movements using MediaPipe's face mesh.
  - Maps eye gaze to screen coordinates to control the mouse pointer.

- **Click Detection**:
  - Detects eye blinking to simulate mouse clicks.

- **Accuracy Metrics**:
  - Calculates and displays:
    - Mouse movement accuracy.
    - Click detection accuracy.
    - Overall system accuracy.

- **Data Logging**:
  - Logs results (target coordinates, landed coordinates, and click data) to a CSV file for performance analysis.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `OpenCV`: For image capture and processing.
  - `MediaPipe`: For facial landmark detection and eye tracking.
  - `PyAutoGUI`: For controlling the mouse pointer and simulating clicks.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  ```bash
  pip install opencv-python mediapipe pyautogui
  ```

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/eye-controlled-mouse.git
   cd eye-controlled-mouse
   ```

2. **Run the Program**:
   ```bash
   python eye_controlled_mouse.py
   ```

3. **Control the Mouse**:
   - Move your eyes to control the mouse pointer.
   - Blink to simulate a mouse click.

4. **Exit the Program**:
   - Press the `q` key to exit.

---

## File Structure

- `eye_controlled_mouse.py`: Main Python script for the eye-controlled mouse system.
- `results.csv`: Logs of target coordinates, landed coordinates, and click data.

---

## Accuracy Metrics

The program computes the following accuracy metrics:

1. **Mouse Movement Accuracy**:
   - Based on the distance between the target coordinates and the actual landed coordinates.
2. **Click Detection Accuracy**:
   - Compares the number of intentional and detected clicks.
3. **Overall System Accuracy**:
   - Weighted combination of movement and click accuracies.

---

## Sample Output

### Console Output
```
Mouse Accuracy: 95.32%
Click Detection Accuracy: 96.00%
Overall System Accuracy: 98.23%
```

### CSV Log Format
```
Target_X,Target_Y,Landed_X,Landed_Y,Click_Detected,Click_Intended
400,300,410,290,1,1
```

---

## Potential Enhancements

- Add support for advanced gestures (e.g., drag-and-drop).
- Optimize for higher accuracy with better calibration techniques.
- Extend functionality to include voice commands.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- **MediaPipe**: For providing robust face and eye-tracking solutions.
- **PyAutoGUI**: For easy mouse automation.

---

## Contribution

Feel free to fork the repository and contribute to this project. Pull requests are welcome!

---

## Contact

For questions or feedback, reach out to **[Harsh Maurya]** at [harshmaurya0509@gmail.com].
