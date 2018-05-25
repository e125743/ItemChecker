#引数（テストデータが入ったフォルダの名前）が無かったら終了。
if ARGV[0].nil?
  printf("Usage: # ruby autoExe.rb TestDataFolderName\n")
  exit!
end

Dir.chdir('./' + ARGV[0])
testFiles = Dir.glob('*')
Dir.chdir('../')
#puts testFiles 

`rm -fr ResultData/Move`
`rm -fr ResultData/NoMove`
`mkdir ResultData/Move`
`mkdir ResultData/NoMove`

for fileName in testFiles do
  puts "#{ARGV[0]}\/#{fileName}"
  #`python ./testCut.py #{ARGV[0]}\/#{fileName}`
  `python ./CheckerExe.py #{ARGV[0]}\/#{fileName}`
end