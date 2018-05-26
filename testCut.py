# coding: UTF-8
import cv2
import numpy as np
import sys

def cut(filepath):
    #画像を取得
    img = cv2.imread(filepath)

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
    filename = filepath.split('/')[-1]
    #print(filename)

    #切り取った画像をウィンドウで出力。
    #cv2.imshow('detected circles',roi)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #切り取った画像を保存。
    cv2.imwrite('CutData/' + filename, roi)

if __name__ == "__main__":
    argvs = sys.argv

    if (len(argvs) <= 1):
      print('Usage: # python %s TestDataFilePath' % argvs[0])
      quit()
    cut(argvs[1])
