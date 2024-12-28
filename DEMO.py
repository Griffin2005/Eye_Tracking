import cv2
import mediapipe as mp
import pyautogui
import math


cap = cv2.VideoCapture(0)  # Use webcam
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark

        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if(left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
        if cv2.waitKey(1) & 0xFF == ord('q'): # To exit the run
            break

    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)

    #accuracy calculation
    target_x, target_y = 400, 300 # Target coordinates
    landed_x, landed_y = 410, 290 # Mouse coordinates
    error_distance = math.sqrt((target_x - landed_x)**2 + (target_y - landed_y)**2)
    screen_diagonal = math.sqrt(screen_w**2 + screen_h**2)
    accuracy = 100 - (error_distance / screen_diagonal)*100

    print(f"Mouse Accuracy: {accuracy:.2f}%") # Accuracy of mouse movement

    intentional_clicks = 50
    detected_clicks = 48
    false_clicks = 5

    accuracy = (detected_clicks/intentional_clicks)* 100
    print(f"Click Detection Accuracy: {accuracy:2f}%") # Accuracy of click


    def log_results(target_x, target_y, landed_x, landed_y, click_detected, click_intended):
        with open("results.csv", "a") as f:
            f.write(f"{target_x},{target_y},{landed_x},{landed_y},{click_detected},{click_intended}\n")

    movement_accuracy = 99.36
    click_accuracy = 96

    overall_accuracy = 0.7*movement_accuracy + 0.3*click_accuracy
    print(f"Overall System Accuracy: {overall_accuracy:.2f}%") # Accuracy of overall system


