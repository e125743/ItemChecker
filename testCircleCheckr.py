# coding: UTF-8
import cv2
import numpy as np
import sys

argvs = sys.argv

if (len(argvs) <= 1):
  print('Usage: # python %s TestDataFilePath' % argvs[0])
  quit()

#画像をグレースケール(,0)で取得。
img = cv2.imread(argvs[1],0)
#メディアンフィルタを適用。
img = cv2.medianBlur(img,3)
#色配列をグレースケールからBGR（OpenCV規格）へ変換。
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#'有'の場合のパラメータ
#circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                            param1=30,param2=30,minRadius=10,maxRadius=0)
#'無'の場合のパラメータ
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=28,param2=31,minRadius=10,maxRadius=0)

print(type(circles))
#丸が検出できた場合の処理。
if type(circles) is not type(None):
  circles = np.uint16(np.around(circles))
  #画像に丸を描写。
  for i in circles[0,:]:
      #丸の曲線を緑色で描写。
      cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
      #丸の中心点を赤色で描写。
      cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

  #結果をウィンドウで出力。
  cv2.imshow('detected circles',cimg)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
