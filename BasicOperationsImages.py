import cv2
import numpy as np
#图像属性、像素属性、图像区域（list或者array.item和itemset）及扩展边界（镜像、墙纸等）
img = cv2.imread("img/opencv-logo.png")
# img.itemset((150,100,0),100)
img[:,:,2]=0
cv2.imwrite("img/opencv-logo1.png",img)
px = img[150,10]

print(px)