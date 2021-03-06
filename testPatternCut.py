# coding: UTF-8
import cv2
import numpy as np
import sys

def patternCut(filepath):
    #画像をグレースケール(,0)で取得
    img = cv2.imread(filepath,0)

    #切り取り画像の左上のpixel
    #'無'の左上のpixel
    x, y = 720, 4070

    #切り取り画像の幅と高さのpixel数
    #'無'の切り取りpixel数
    w = 775
    h = 150

    #画像から切り取り実行
    roi = img[y:y+h, x:x+w]

    #画像から項目欄の左端の縦枠のpixelを推定。
    leftPixel = -1
    #画像上端から下方向にpixel行を取得。
    for sh in range(h):
      #pixel行の左端から右方向にpixelを取得。
      for sw in range(w):
        #取得したpixelが黒っぽい色をしていた時且つ、
        #その下の50pixelの内、40pixelが黒っぽい色をしていた時の処理。
        if roi[sh, sw] < 100 and 255*10 > np.sum(roi[sh:sh+50, sw]):
          leftPixel = sw
          break
      #leftPixelに数値が入ったら終了。
      if leftPixel != -1:
        break
    print(leftPixel)

    #画像から項目欄の下端の横枠のpixelを推定。
    underPixel = -1
    #画面右端から左方向にpixel列を取得。
    for sw in range(w-1, 0, -1):
      #pixel列の下端から上方向にpixelを取得。
      for sh in range(h-1, 0, -1):
        #取得したpixelが黒っぽい色をしていた時且つ、
        #その左の50pixelの内、40pixelが黒っぽい色をしていた時の処理。
        if roi[sh, sw] < 100 and 255*10 > np.sum(roi[sh, sw-50:sw]):
          underPixel = sh
          break
      #underPixelに数値が入ったら終了。
      if underPixel != -1:
        break
    print(underPixel)

    #縦枠と横枠が交わるpixelから内側に10pixel動かし、枠を画像から消去。
    patternRoi = roi[underPixel-85:underPixel-10, leftPixel+10:leftPixel+400]

    #for ro in patternRoi:
    #  print(ro)

    #filepathからファイル名を取得
    filename = filepath.split('/')[-1]
    #print(filename)

    #切り取った画像をウィンドウで出力。
    #cv2.imshow('detected circles',roi)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #切り取った画像を保存。
    cv2.imwrite('CutData/' + filename, patternRoi)

if __name__ == "__main__":
    argvs = sys.argv

    if (len(argvs) <= 1):
      print('Usage: # python %s TestDataFilePath' % argvs[0])
      quit()
    patternCut(argvs[1])
