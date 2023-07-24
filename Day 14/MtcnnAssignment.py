import cv2
from mtcnn import MTCNN
detector= MTCNN()
img = cv2.imread('holiday_groupimage-scaled2.jpg')
output= detector.detect_faces(img)
x,y,w,h = output[0]['box']
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imshow('gv',img)
cv2.waitKey(0)