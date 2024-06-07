import cv2
import numpy as np
import pyautogui

# Set up the video writer
screen_size = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_recording.avi", fourcc, 20.0, (screen_size.width, screen_size.height))

try:
    while True:
        # Capture the screen
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write the frame to the video file
        out.write(frame)

        # Display the recording screen (optional)
        cv2.imshow("Recording", frame)

        # Stop recording on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass

# Release everything
out.release()
cv2.destroyAllWindows()
