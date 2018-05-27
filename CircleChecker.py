# coding: UTF-8
import cv2
import numpy as np
import sys

def circleChecker(cutImage, fileName):
    #メディアンフィルタを適用。
    img = cv2.medianBlur(cutImage,5)
    #色配列をグレースケールからBGR（OpenCV規格）へ変換。
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    #'有'の場合のパラメータ
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
    #                            param1=30,param2=30,minRadius=10,maxRadius=0)
    #'無'の場合のパラメータ
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=28,param2=31,minRadius=10,maxRadius=0)

    saveDir = 'ResultData/'
    print(type(circles))
    #丸が検出できた場合の処理。
    if type(circles) is not type(None):
      circles = np.uint16(np.around(circles))
      #丸を描写。
      for i in circles[0,:]:
        #丸の曲線を緑色で描写。
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        #丸の中心点を赤色で描写。
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
      saveDir += 'NoMove/'
    #丸が検出されなかった場合の処理。
    else:
      saveDir += 'Move/'
      cimg = cutImage

    print(saveDir)
    cv2.imwrite(saveDir + fileName, cimg)



def cut(filePath):
    #画像をグレースケール(,0)で取得
    img = cv2.imread(filePath,0)

    #切り取り画像の左上のpixel
    #'有'の左上のpixel
    #x, y = 745, 3925
    #'無'の左上のpixel
    x, y = 745, 4070

    #切り取り画像の幅と高さのpixel数
    #'有'の切り取りpixel数
    #w = 250#1805
    #h = 115
    #'無'の切り取りpixel数
    w = 400
    h = 120

    #画像から切り取り実行
    roi = img[y:y+h, x:x+w]

    #filepathからファイル名を取得
    fileName = filePath.split('/')[-1]
    #print(fileName)

    return roi, fileName

if __name__ == "__main__":
    argvs = sys.argv

    if (len(argvs) <= 1):
      print('Usage: # python %s TestDataFilePath' % argvs[0])
      quit()
    cutImage, fileName = cut(argvs[1])
    circleChecker(cutImage, fileName)
