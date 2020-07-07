import cv2
import numpy as np

img = np.zeros((700,500,3),np.uint8)
cv2.rectangle(img,(20,20),(120,120),(0,255,255),5)
cv2.circle(img,(300,70),50,(0,255,0),5)

pts = np.array([[50,200],[50,400],[180,400]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,0,255),3)

cv2.putText(img,"TEST",(220,350),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,3,(255,0,0),3)
cv2.imshow("1",img)
cv2.imwrite("img/Geometry.png", img)
cv2.waitKey(0)