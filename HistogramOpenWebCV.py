import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    equ = cv2.equalizeHist(gray)
    res = np.hstack((gray,equ))

    cv2.imshow('frame',res)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()