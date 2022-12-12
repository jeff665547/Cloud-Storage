from argparse import ArgumentParser
# argparse模組使用主要分三步：
# 1. 建立 ArgumentParser() 物件
# 2. 呼叫 add_argument() 方法新增引數
# 3. 使用 parse_args() 解析新增的引數
# 加入定位引數(即程式碼寫完後直接按照引數加入順序加在檔名後方
# e.g. python parser1.py 66 中的 66 即自動解析到integer屬性中，
# 就是一般sys.argv的概念啦，不可省略，所有的定位引數都要下完)
parser1 = ArgumentParser()
parser1.add_argument("integer1", help = "display an integer.", default = 11, type = int)
parser1.add_argument("integer2", help = "display an integer.", default = 22, type = int)
args1 = parser1.parse_args()

print('the parameter is: ', args1)