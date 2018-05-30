require "open3"

#引数（テストデータが入ったディレクトリの名前）が無かったら終了。
if ARGV[0].nil?
  printf("Usage: # ruby autoExe.rb TestDataFolderName\n")
  exit!
end

#ディレクトリを移動。
Dir.chdir('./' + ARGV[0])
#ディレクトリ内のテストデータを取得。
testFiles = Dir.glob('*')
#元居たディレクトリに移動。
Dir.chdir('../')
#puts testFiles 

#解析結果が既にあったら上書き。
`rm -fr ResultData/Move`
`rm -fr ResultData/NoMove`
`mkdir ResultData/Move`
`mkdir ResultData/NoMove`

margins = []

#実行プログラムにテストデータを引数として渡す。
for fileName in testFiles do
  puts "#{ARGV[0]}\/#{fileName}"
  #`python ./testCut.py #{ARGV[0]}\/#{fileName}`
  #`python ./CircleChecker.py #{ARGV[0]}\/#{fileName}`
  #`python ./testPatternCut.py #{ARGV[0]}\/#{fileName}`
  `python ./MarginChecker.py #{ARGV[0]}\/#{fileName}`

  #testMargin.pyは実行結果を表示。
  #o, e, s = Open3.capture3("python ./testMargin.py #{ARGV[0]}\/#{fileName}")
  #puts o
  #margins.push(o.to_i)
end


#testMargin.pyの実行結果を解析
#p margins.max
#p margins.min
#p margins.max - margins.min
#p margins.inject{|r,i| r+=i }/margins.size