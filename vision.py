import cv2
import numpy as np
import mss
import time

# Define the capture region (use actual game coordinates if known)
monitor = {"top": 100, "left": 100, "width": 1280, "height": 720}

with mss.mss() as sct:
    while True:
        start_time = time.time()

        # Capture screen
        sct_img = sct.grab(monitor)

        # Convert to numpy array and BGR for OpenCV
        frame = np.array(sct_img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # Display
        cv2.imshow("Botan's Vision", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Optional: show FPS
        fps = 1 / (time.time() - start_time)
        print(f"FPS: {fps:.2f}", end="\r")

cv2.destroyAllWindows()
