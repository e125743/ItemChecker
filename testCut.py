# coding: UTF-8
import cv2
import numpy as np
import sys

def cut(filepath):
    #画像を取得
    img = cv2.imread(filepath)

    #切り取り画像の左上のpixel
    x, y = 800, 4050

    #切り取り画像の幅と高さのpixel数
    w, h = 250, 125

    #画像から切り取り実行
    roi = img[y:y+h, x:x+w]

    #filepathからファイル名を取得
    filename = filepath.split('/')[-1]
    #print(filename)

    #画像を表示
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
