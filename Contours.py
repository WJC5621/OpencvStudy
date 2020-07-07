import cv2
import numpy as np
import os
b = (0,255,0)
img = cv2.imread('img/Geometry.png', 0)
#ret,dst = cv2.threshold(img,1,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
imgContours = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
imgContours = cv2.drawContours(imgContours,contours,-1,(0,0,255),1)
cv2.imshow("img/imgContours", imgContours)
for contour in contours:
    #矩形框
    # x, y, w, h = cv2.boundingRect(contour)
    # imgRect = cv2.rectangle(imgContours, (x, y), (x + w, y + h), (0, 255, 0), 1)
    #最小包围矩形
    # retval = cv2.minAreaRect(contour)
    # points = cv2.boxPoints(retval)
    # points = np.int0(points)
    # print(points)
    # imgMinAreaRect = cv2.drawContours(imgContours,[points],0,(0,255,0),1)
    #圆
    # (x,y),radius = cv2.minEnclosingCircle(contour)
    # cv2.circle(imgContours,(int(x),int(y)),int(radius),b,1)
    # #最小三角形
    # area,triangle = cv2.minEnclosingTriangle(contour)
    # #查看对象数据类型  type(p)
    # #查看np array的样式p.shape
    # triangle = np.int0(triangle)
    # triangle=triangle.reshape(-1,2) #对triabgle进行重塑由由原本的（3，1，2）重塑为二维数组
    # cv2.drawContours(imgContours,[triangle],0,b,1)
    # cv2.polylines(imgContours,[np.int0(triangle)],True,b,1)  #使用drawContours和polylines均可实现
    #椭圆
    # retval = cv2.fitEllipse(contour)
    # print(retval)
    # cv2.ellipse(imgContours,retval,b,1)
    #外接多边形
    epsilon = 0.1*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)
    print(approx)
    cv2.drawContours(imgContours,[approx],0,b,1)
cv2.imshow("img",imgContours)
#cv2.imwrite(os.sep.join(["img","contours","imgEllipse.png"]),imgContours)
cv2.waitKey(0)
"""1.二值化图像
2.二值化图像
3.寻找轮廓
4.绘画轮廓/找外接矩形、最小外接矩形、最小外接圆、椭圆、多边形/凸包、凸缺陷
"""
