# coding: UTF-8
import cv2
import numpy as np
import sys

def margin(filepath):
    #画像をグレースケール(,0)で取得
    img = cv2.imread(filepath,0)

    print(np.sum(img))

if __name__ == "__main__":
    argvs = sys.argv

    if (len(argvs) <= 1):
      print('Usage: # python %s TestDataFilePath' % argvs[0])
      quit()
    margin(argvs[1])
