import cv2
import numpy as np
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
drawing = False # true if mouse is pressed
mode = 0 # 0、1、2分别画矩形、圆、三角形
ix,iy = [],[]

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    i = 0
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix[i],iy[i] = x,y
        i+=1

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),20,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 0:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        elif mode == 1:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
        else:
            cv2.fillPoly(img,((ix,iy),(x,y)),(0,255,0),-1)
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('img/Geometry.png', img)
cv2.destroyAllWindows()
