# ItemChecker

# 概要
アンケートや住居変更などの書類を自動で仕分けるためのプログラム。  
特定項目（例えば'有' か '無'）に丸が付けられているかどうかで書類を仕分けたいと試みています。

# 環境
Python2  
Ruby  
OpenCV

# ソースの説明
* testCut.py  
書類の特定の箇所を切り出して表示する為のプログラム。  
特定項目の部分が上手く切り出せるように適切な切り取りパラメータ（プログラム内のx, y, w, h）を探して下さい。
```
mkdir Cutdata #初回の一回のみ実行
python testCut.py "テスト用画像ファイル"
```

* testCircleChecker.py  
特定項目に丸が付けられているかを判定する為のプログラム。  
testCut.pyで切り取った画像で何度か試し、適切なパラメータ（プログラム内のcv2.HoughCirclesに与えるパラメータ）を探して下さい。
```
python testCircleChecker.py "testCut.pyで切り取った画像ファイル"
```

* CircleChecker.py  
本番用のプログラム。  
プログラム内のパラメータ（x, y, w, h, cv2.HoughCirclesに与えるパラメータ）をtestCircleChecker.pyとtestCut.pyで探したパラメータにそれぞれ書き換えて下さい。  
書類を特定項目に丸が付いている物（ResultData/Move）と付いていない物（ResultData/NoMove）に分けます。

* autoExe.rb  
実行用のプログラム。  
```
mkdir ResultData #初回の一回のみ実行
ruby autoExe.rb "仕分けしたい書類ファイルを入れたディレクトリ"
```