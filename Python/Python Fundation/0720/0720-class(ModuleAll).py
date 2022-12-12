#模組(Importing and Modules)
#若要安裝Python 64位元的版本，請至官網找到想下載的Python版本，並在裡面找"Windows x86-64 executable installer"下載，安裝時為了後須方便處裡，請注意要勾選"Add Python3.X to Path"
#內建模組、自訂模組、第三方模組



#模組其實就是.py檔，任何一個.py檔儲存起來都可以被稱作是模組，而這個.py檔裡面可能定義了函數、類別、變數等內容
#可以藉由import指令來將以前寫過的py檔匯入到目前正在撰寫的程式中
#匯入模組(兩種語法: 1. import module1, module2, module3, ......)  => 和下方的語法等價
#       (          2. from modname import name1, name2, mame3, ......)  => 想要更精確地去指出想要用哪一個模組裡面的哪一個函數

#如果import的模組名稱太長或是不喜歡，可以使用import...(old name) as...(new name)去替換這個模組在自己這隻程式碼所使用的名稱        

#內建模組 math
import math as ma #將math模組重新命名成ma
print(ma.pi)  #印出ma模組(math)裡面的pi

#內建模組 sys
import sys
print(sys.path)

#在Windows中，模組的存放位置
#  安裝Python的資料夾路徑/Lib

#在Linux中，模組的存放位置
#   /usr/lib/python2.x(python3.x)

#好用內建模組 time
import time
time.time() #取得系統時間

time.sleep(3) #設定系統暫停3(sec)
time.localtime()

time.strftime(TimeFormat)  #格式化輸出時間
time.gmtime #取得UTC世界標準時間

help(time.strftime)

#自訂模組
#omitted

#第三方程式庫的使用與安裝(代表電腦裡面沒有內建)

#第一種:下載原始碼，然後使用python setup.py install 做安裝
#第二種:使用pip 或 easy_install 還有 distribute 等(第三方套件管理程式)方法  (需要自己加path)
#要注意套件的版本及適合的python版本(python2 or python3)以及位元還有目前所使用的作業系統(windows or linux)
#PyPI (Python Package Index)，Python 的第三方套件集散地，官方把所有的套件都集合在這裡,使用pip管理
#網址:https://pypi.python.org/pypi?:action=browse&c=533&show=all

#Install package method 1: basic installation (Python setup.py install)
#ex.產生QR code (QR code產生器 只要是文字文件都可以，or 圖片網址)
#先測試此電腦上是否安裝該package : import pyqrcode 
#若沒安裝則會出現ModuleNotFoundError，接著便可進行以下安裝步驟，若沒有跑出任何的error，則代表此電腦已經有安裝該package了
#PyQRCode package 網址:https://pypi.python.org/pypi/PyQRCode
#step1: 先到想安裝的package網址下載該package的壓縮檔
#step2: 將該壓縮檔給解壓縮
#step3: 打開cmd(commander) (Windows) or terminal (Mac, Linux)
#step4: 複製剛剛解壓縮檔的資料夾路徑，接著打上cd 該資料夾路徑，進到該資料夾裡面，e.g.: cd C:\Users\jeff\Desktop\PyQRCode-1.2.1
#       或是直接先用滑鼠點到該資料夾裡面的介面，並且在該資料夾上方路徑的位置直接打cmd，接著就會跳出cmd，而且工作路徑也會跟著改變，和上面的方法有相同的效果
#step5: 在command line上打python，進入python，這一步是要確認python的版本(3.6.0)，以及裝在甚麼作業系統以及其版本(.... on win32)上
#step6: 確認完後離開python(Windows:control + z)
#step7: 跳出python後在command line上打python 該資料夾裡的系統安裝檔名稱(e.g.setup.py) install
#       也就是python setup.py install，打完後按Enter
#step8: 從cmd的命令列中確認package是否安裝成功，請看剛剛安裝所跑出來的最後幾行中Installed + 安裝路徑位置  開頭後面的指令成功的話應該會有finished的一些指令
#step9: 接著，若原本是有打開python的話，請將python先關閉，接著再重新打開python即可使用，若原本是在沒有開啟python的情況下安裝上述步驟，則可忽略此步驟，直接開啟python便可使用
#step10: 輸入import 剛剛安裝的package名稱即可匯入該模組套件
#step11: 該套件的使用方式可以參考該package裡面的Usage部分
import pyqrcode
url = pyqrcode.create('https://worldoftanks.asia/dcont/fb/image/aug_2013_2560x1600-8.jpg') #可放想產生QR code的網址 e.g. Conqueror的海報圖片
url.svg('url.svg', scale = 8)  #scale代表圖片尺寸大小
url.eps('url.eps', scale = 8)  
url.png('url.png', scale = 8)  #存成png檔 scale代表圖片尺寸大小
#跑完之後就會存檔，再去網頁檔開即可
#注意在跑png檔時很有可能會出現錯誤，因為必須要先安裝pypng的套件才能夠跑上面的指令
#pypng package 網址: https://pypi.python.org/pypi/pypng


#Install package method 2: Use PIP packages to install(The most popular method)
#注意:此方法需要先用上述的 method 1 安裝pip套件管理的套件
#pip package 網址: https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz
#step1: 先到想安裝的package網址下載該package的壓縮檔
#step2: 將該壓縮檔給解壓縮
#step3: 打開cmd(commander) (Windows) or terminal (Mac, Linux)
#step4: 複製剛剛解壓縮檔的資料夾路徑，接著打上cd 該資料夾路徑，進到該資料夾裡面，e.g.: cd C:\Users\jeff\Desktop\pip-1.3.1
#step5: 在command line上打python，進入python，這一步是要確認python的版本(3.6.0)，以及裝在甚麼作業系統以及其版本(.... on win32)上
#step6: 確認完後離開python(Windows:control + z)
#step7: 跳出python後在command line上打python 該資料夾裡的系統安裝檔名稱(e.g.setup.py) install
#       也就是python setup.py install，打完後按Enter
#
#以上為在電腦中安裝pip的步驟，接下來是確認pip是否正確安裝以及運用pip去裝其他的套件(通常pip會內建在python的最新版本(python3)裡面)
#
#step8: 確認pip有正確安裝: 在command line直接輸入pip(Mac or Linux: pip3 or pip3.4)，若安裝成功則會列出很多的相關資訊，若沒有安裝成功，則command line裡會出現 "'pip' 不是內部或外部命令、可執行的程式或批次檔。" 等相關的語句。
#       若安裝完後仍然不能正常使用(出現上面的訊息)，請把pip的所在目錄(通常是在C:\Python34\Scripts\裡面)給加到執行目錄裡面，這樣子才可以在任何地方使用pip(Mac or Linux: pip3 or pip3.4)這個指令，以下為操作方法
#       step8-1: 打開pip.py的所在目錄，把路徑給複製下來(C:\Python34\Scripts)
#       step8-2: 對"電腦(我的電腦、本機)"按右鍵，打開"內容"，並到左側的側邊欄中選取"進階系統設定"
#       step8-3: 接著會跳出一個新的視窗，請在這個視窗上面的標籤頁上選擇"進階"這個標籤頁
#       step8-4: 接著在此標籤頁的下半部有一個"環境變數"的按鈕選項，點下去，會跳出一個新的視窗，名為"環境變數"
#       step8-5: 在這個視窗中分成上下兩個部分，上面的部分是針對"user的使用者變數"，下面的部分則是"系統變數"，更改上面的user變數，則更改發揮的作用只有針對這一位特定的使用者。然而，若是針對下方的系統變數做更動，則代表更改發揮的作用是針對所有使用這台電腦的使用者
#                請在"系統變數"中點選"Path"變數，接著點選下方的"編輯"鈕，會跳出"編輯系統變數"的視窗
#       step8-6: 在這個視窗中的"變數值"欄位中，若在這一大堆路徑碼裡沒有"C:\Python34\Scripts;以及C:\Python34;"(是根據step8-1裡pip.py的所在目錄，每一個版本放的位置都不同)的話，請幫系統加入此路徑(若有需要，請使用";"和已存在的路徑做區隔，貼完此路徑也請在加";"來做新加入路徑的結尾)，若有即可忽略此步驟
#       step8-7: 以上若都設定完成後，請對所有已打開的視窗按"確定"按鈕，即完成pip 的安裝
#
#step9: 在順利安裝完pip之後，即可加入想加的模組與套件 pip(pip3) install 想裝的package name (e.g.pip(pip3) install pypng)
#       注意: pip3.4 or pip3 的寫法較好，因為可以告知系統要把這些套件以及模組裝在哪一個Python版本裡面
#
#step10: 按下Enter後即安裝完成，便可以開始使用該套件，若安裝過程中出現問題，請參考以下說明
#注意: 有些package用pip安裝不起來，這時請至網路上下載*.whl檔(需去對應所使用的python版本)即可安裝
#      step10-1: e.g. scipy的話，在google打scipy whl，然後去"Unofficial Windows Binaries for Python Extension Packages"下載對應的Python版本即可，Numpy的話，在google打numpy mkl whl，然後去下載"Unofficial Windows Binaries for Python Extension Packages"對應的Python版本
#      step10-2: 下載完成後請將下載檔案的路徑給複製下來(e.g.: C:\Users\jeff\Downloads)至cmd的command line打 pip(pip3) install 剛剛下載下來檔案的路徑位置(e.g.: C:\Users\jeff\Downloads\numpy-1.13.1+mkl-cp27-cp27m-win32.whl)  (e.g.pip3 install C:\Users\jeff\Downloads\numpy-1.13.1+mkl-cp27-cp27m-win32.whl)
#      step10-3: 按下Enter鍵即可完成
#注意: 若有出現存取被拒的情形，請先使用"以系統管理員身分執行"cmd即可避免該問題發生

#Install package method 3: Use conda to install (conda套件與環境管理工具)
#step1: 打開Anaconda Prompt ，開啟後可以看到其介面如同命令提示字元一樣，最前面的括號內代表的是在哪個環境之下，後面(括號外)則代表目前的位置
#step2: 先更新conda package管理系統(順便查看conda是否能夠正常運作,若不行，通常是因為當時在灌Anaconda時，安裝的對象設置成是"對所有使用者"，應該要是"僅對這個使用者Just me"這個選項才對) 在command line 上輸入 conda update conda
#step3: 安裝想安裝的套件: conda install (package名稱) (e.g. conda install numpy)
#step4: 完成


#使用Jupyter network
#step1: 打開Anaconda Prompt ，開啟後可以看到其介面如同命令提示字元一樣，最前面的括號內代表的是在哪個環境之下，後面(括號外)則代表目前的位置
#step2: 找到想要的工作路徑資料夾，並且把路徑位置給複製下來貼到Anaconda Prompt的command line  中，並且用cd移到該路徑位置資料夾，之後所有有關該程式的輸出都會存放在這個工作路徑中(讀檔也會比較方便，可以使用相對路徑)
#step3: 使用Anaconda Prompt 並且cd到想要工作的工作路徑之後，接著請直接在command line上面輸入"jupyter notebook"後系統即會使用瀏覽器開啟jupyter notebook了
#step4: 在打開jupyter notebook 後，找到想要編輯的檔案後，便可以開始編輯，如要新增一個Python3的檔案，請至該介面的右上角的"New"的選單中，在"Notebook:"的選單裡選取Python3
#step5: 完成上述步驟後，便可發現此時的存檔為.ipynb檔，這屬於正常現象，該檔案類型格式支援github，可做一些對使用者友善的顯示功能(類似markdown的效果)。


#Uninstall package  解除安裝package
#step1: 利用上述方法確認已有安裝pip package
#step2: 打開cmd，並在command line 輸入 pip(pip3) uninstall (想解除安裝的package名稱)，e.g.:(pip(pip3) uninstall pypng)
#step3: 在解除安裝中輸入"y"確認解除安裝該package即完成


#在Anaconda的spyder中安裝package
#step1: 打開spyder 在上面的選單中按"Tools"裡的"Open command prompt"(相當於cmd)
#step2: 確認安裝pip(pip3)  在command line上直接打pip(pip3)
#step3: pip(pip3) install ......(package name)

#e.g.Matplotlib Package 3D數據繪圖軟件(須於Python的IDLE中另外開新檔才能使用完整功能)
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)

plt.show()

