#引数（テストデータが入ったフォルダの名前）が無かったら終了。
if ARGV[0].nil?
  printf("Usage: # ruby autoExe.rb TestDataFolderName\n")
  exit!
end

Dir.chdir('./' + ARGV[0])
testFiles = Dir.glob('*')
#puts testFiles 

