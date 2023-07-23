import cv2
cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    print(_)
    cv2.imshow("video", frame)
    cv2.waitKey(1)