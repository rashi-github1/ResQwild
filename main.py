import cv2
import numpy as np
import serial  # For communication with Arduino
import time

# Function to initialize serial communication
def initialize_serial(port, baud_rate, retries=5, delay=2):
    for attempt in range(retries):
        try:
            ser = serial.Serial(port, baud_rate, timeout=1)
            time.sleep(delay)  # Wait for the connection to initialize
            print(f"Arduino is connected on {port}")
            return ser
        except serial.SerialException as e:
            print(f"Error: {e}. Retrying ({attempt + 1}/{retries})...")
            time.sleep(delay)
    print(f"Failed to connect to Arduino on {port}")
    return None

# Initialize serial communication with Arduino
port = 'COM9'  # Adjust COM port as needed
baud_rate = 9600
arduino = initialize_serial(port, baud_rate)

# Load the object detection model
model = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")

# Define the list of object classes
classes = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # Access the default camera
#address = "http://192.0.0.4:8080/video"  # Update the IP camera address if needed
#cap.open(address)
def capture_image(frame):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"detected_animal_{timestamp}.jpg"
    success = cv2.imwrite(filename, frame)
    if success:
        print(f"Image saved as {filename}")
    else:
        print(f"Failed to save image as {filename}")

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame, check camera connection.")
        break

    # Preprocess the frame
    frame_height, frame_width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)

    # Pass the frame through the model
    model.setInput(blob)
    detections = model.forward()

    # Loop through the detections
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            # Get the class ID and label
            class_id = int(detections[0, 0, i, 1])
            class_label = classes[class_id]

            # Get the bounding box coordinates
            box = detections[0, 0, i, 3:7] * np.array([frame_width, frame_height, frame_width, frame_height])
            (startX, startY, endX, endY) = box.astype("int")

            # Draw the bounding box and label on the frame
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, f"{class_label} {confidence * 100:.2f}%", 
                        (startX, startY - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Check if the detected object is a lion, tiger, or bear (mapped to "cat" or "dog")
            if class_label in ["cat", "dog"]:  # "cat" for lion/tiger and "dog" for bear
                print(f"{class_label} detected, sending signal to Arduino...")

                if arduino:  # Ensure Arduino is connected
                    try:
                        arduino.write(b'1')  # Send '1' to Arduino to trigger servo and alarm actions
                    except serial.SerialException as e:
                        print(f"Failed to send data to Arduino: {e}")

                capture_image(frame)  # Capture and save the image when the animal is detected

    # Display the frame
    cv2.imshow("Object Detection", frame)

    # Check for key presses
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

# Close the serial connection
if arduino:
    arduino.close()
