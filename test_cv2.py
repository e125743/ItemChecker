# coding: UTF-8
import cv2
import numpy as np

#画像をグレースケール(,0)で取得。
img = cv2.imread('CircleTest.jpg',0)
#メディアンフィルタを適用。
img = cv2.medianBlur(img,3)
#色配列をグレースケールからBGR（OpenCV規格）へ変換。
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=30,param2=20,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
