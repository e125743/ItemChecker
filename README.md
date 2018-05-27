# ItemChecker

# 概要
アンケートや住居変更などの書類を自動で仕分けるためのプログラム。  
特定項目（例えば'有' か '無'）に丸が付けられているかどうか、  
丸が付けられていない画像と付けられている画像との余白の違いを比較  
で書類を仕分けたいと試みています。

# 環境
Python2  
Ruby  
OpenCV

# プログラムの説明
<br>
<br>
<br>
  
##### - 丸検出を使ったプログラム
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
`python testCircleChecker.py "testCut.pyで切り取った画像ファイル"`

* CircleChecker.py  
本番用のプログラム。  
プログラム内のパラメータ（x, y, w, h, cv2.HoughCirclesに与えるパラメータ）をtestCircleChecker.pyとtestCut.pyで探したパラメータにそれぞれ書き換えて下さい。  
書類を特定項目に丸が付いている物（ResultData/Move）と付いていない物（ResultData/NoMove）に分けます。
<br>
<br>
<br>
  
##### - 余白の違いを使ったプログラム
* testPatternCut.py  
書類の特定項目の左縦枠、下横枠を削除した画像を作成するプログラム。  
testCut.pyで特定項目の左縦枠と下横枠のみが上手く入るように適切な切り取りパラメータ（プログラム内のx, y, w, h）を探して下さい。  
その後、testPatternCut.pyのプログラム内のパラメータx, y, w, hをtestCut.pyで探したパラメータに書き換えて下さい。  
最後に、プログラム内のpatternRoiに入れる配列roiの添字  
`underPixel-85:underPixel-10, leftPixel+10:leftPixel+400`  
を、特定項目の左縦枠、下横枠を削除出来るように整数部分を調整して下さい。
```
mkdir Cutdata #初回の一回のみ実行
python testPatternCut.py "テスト用画像ファイル"
```

* testMargin.py  
画像をグレースケールで読み込んだ時の総ピクセル数を出力するプログラム。  
`python testMargin.py "testPatternCut.pyで切り取った丸が付いていない画像ファイル"`

* MarginChecker.py  
本番用のプログラム。  
プログラム内のパラメータx, y, w, hをtestPatternCut.pyで探したパラメータに書き換えて下さい。  
また、プログラム内のnonCircleの中に、丸が付いていない画像の総ピクセル数（testMargin.pyを使って算出した数値）を入れて下さい。  
書類を特定項目に丸が付いている物（ResultData/Move）と付いていない物（ResultData/NoMove）に分けます。
<br>
<br>
<br>
  
##### - 実行用プログラム
* autoExe.rb  
実行用のプログラム。  
丸を丸検出を使ったプログラムを実行する時は25行目 `\#\`python ./testPatternCut.py #{ARGV[0]}\/#{fileName}\``  
余白の違いを使ったプログラムを実行する時は27行目 `\#\`python ./MarginChecker.py #{ARGV[0]}\/#{fileName}\``  
のコメントをそれぞれ外してから、下記のように実行して下さい。
```
mkdir ResultData #初回の一回のみ実行
ruby autoExe.rb "仕分けしたい書類ファイルを入れたディレクトリ"
```