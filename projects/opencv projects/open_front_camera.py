import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flipped_img = cv2.flip(gray, 1)
    # Display the resulting frame
    cv2.imshow('frame', flipped_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
# press 'q' to exit the window
