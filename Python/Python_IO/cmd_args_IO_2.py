from argparse import ArgumentParser
# argparse模組使用主要分三步：
# 1. 建立 ArgumentParser() 物件
# 2. 呼叫 add_argument() 方法新增引數
# 3. 使用 parse_args() 解析新增的引數
# 引數又分為可選引數以及定位引數
# 加入定位引數(即程式碼寫完後直接按照引數加入順序加在檔名後方
# e.g. python parser1.py 66 中的 66 即自動解析到integer屬性中，
# 就是一般sys.argv的概念啦，不可省略，所有的定位引數都要下完)
parser = ArgumentParser()
parser.add_argument("integer1", help = "display an integer.", default = 11, type = int)
parser.add_argument("integer2", help = "display an integer.", default = 22, type = int)

# 加入可選引數(程式碼寫完後須按照選項的指定格式加在檔名後方
# e.g. python parser2.py -o world 中的 -o world 即自動解析到opt屬性中，
# 就是有時會在C++中看到的下參數的感覺，所有參數不是一定都要下，可省略)
# 若無specify dest 則直接以"-"or "--"後方的字或詞當作解析完後的屬性了
parser.add_argument("--gpu", help="GPU device id to use", dest="gpu", default=0, type=int)
parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")
# 代表下-o 或是 --optional-arg這兩種選項的寫法都可以
args = parser.parse_args()

print('the parameter is: ', args)
