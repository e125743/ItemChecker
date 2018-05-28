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

    #for ro in roi:
    #  print(ro)

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

    #filepathからファイル名を取得
    filename = filepath.split('/')[-1]
    #print(filename)

    return filename, patternRoi

def marginChecker(filename, patternRoi):
    #丸が付いていない画像の総ピクセル数を判断基準に設定。
    #testMargin.pyで出力した数値。
    nonCircle = 7069410
    saveDir = 'ResultData/'

    #判断基準より画像の総ピクセル数が小さい時且つ、
    #判断基準と画像の総ピクセル数との差が丸の最小円周より大きい時の処理。
    if abs(nonCircle - np.sum(patternRoi)) > 255*60*3*2 and nonCircle > np.sum(patternRoi):
      saveDir += 'NoMove/'
    else:
      saveDir += 'Move/'

    cv2.imwrite(saveDir + filename, patternRoi)

if __name__ == "__main__":
    argvs = sys.argv

    if (len(argvs) <= 1):
      print('Usage: # python %s TestDataFilePath' % argvs[0])
      quit()
    filename, patternRoi = patternCut(argvs[1])
    marginChecker(filename, patternRoi)
