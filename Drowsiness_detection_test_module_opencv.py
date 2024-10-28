import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
model=YOLO("Drowsiness_Detection_using_YOLOv8.pt")


while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame from webcam.")
        break

    results = model(frame)
        
    cv2.imshow('YOLO Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()