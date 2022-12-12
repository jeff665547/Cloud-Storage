from argparse import ArgumentParser
# argparse模組使用主要分三步：
# 1. 建立 ArgumentParser() 物件
# 2. 呼叫 add_argument() 方法新增引數
# 3. 使用 parse_args() 解析新增的引數
# 加入可選引數(程式碼寫完後須按照選項的指定格式加在檔名後方
# e.g. python parser2.py -o world 中的 -o world 即自動解析到opt屬性中，
# 就是有時會在C++中看到的下參數的感覺，所有參數不是一定都要下，可省略)
# 若無specify dest 則直接以"-"or "--"後方的字或詞當作解析完後的屬性了
parser2 = ArgumentParser()
parser2.add_argument("--gpu", help="GPU device id to use", dest="gpu", default=0, type=int)
parser2.add_argument("-o", "--optional-arg", help="optional argument", default="default")
# 代表下-o 或是 --optional-arg這兩種選項的寫法都可以
args2 = parser2.parse_args()

print('the parameter is: ', args2)