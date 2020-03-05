import cv2

cap=cv2.VideoCapture(0)
while True:

    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    dst = cv2.erode(dst, None, iterations=6)
    cv2.imshow("old",dst)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()