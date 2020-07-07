import numpy as np
import cv2

img = cv2.imread('C:/Users/wu_jch/Pictures/2.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.imread('C:/Users/wu_jch/Pictures/2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('img/img_reload.png', img_gray)
img_reload = cv2.imread('img/img_reload.png')
print(img.shape,img_reload.shape)#将三通道图像以灰度读取后存储，是将灰度复制到三通道
cv2.imshow('img_reload',img_reload)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('img/opencv_log.png',img)
    cv2.destroyAllWindows()