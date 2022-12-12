# PyQt5 訊號與槽
# 此例示範多執行緒中使用訊號與槽
# 最簡單的方法是透過QThread函數
# 執行緒介紹：簡單來說就是運行中的程式
# 此example正在闡述一個情境：當我們在執行一段程式碼中，需要運行其他的小程式時，
# 若把所有的程式碼全部寫在同一份檔案裏面（由上而下編寫），我們很可能會因為運行
# 那個小程式或是其中一段程式碼而造成主程式的delay，此時我們事實上必須等待這個
# 小程式運行完畢才能夠接續運行主程式碼其他剩餘的部分，若能夠獨立讓這兩個程式碼
# 不要互相干擾，而且又能夠互相溝通，則能達到最理想的效果。
# 舉個較常見的例子，小程式是開啟檔案（由使用者選擇），主程式可能是在計算其他東西，
# 但因為使用者遲遲沒有選好指定的檔案，所以導致整個程式的delay，本例就是在幫助我們
# 達到看似使用者還沒有選好指定的檔案，但其餘的程式仍然可以繼續work，不會受到影響，
# 等待使用者選好指定的檔案後，再把新的檔案以及參數傳給主函式，達到平行多工的效果。

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
import sys

class Main(QWidget):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        
        # 建立一個執行緒實例，並設定名稱、變數、訊號與槽
        self.thread = MyThread()                  # 執行__init__()
        self.thread.setIdentity("thread1")        # 執行setIdentity()
        self.thread.sinOut.connect(self.outText)  # 宣告只要sinOut一觸發(emit)就執行outText()
        self.thread.setVal(6)                     # 執行setVal(), start(), run()以及sinOut()
        
    def outText(self, text):
        print(text)

class MyThread(QThread):
    sinOut = pyqtSignal(str)
    
    def __init__(self, parent = None):
        super(MyThread, self).__init__(parent)
        self.identity = None
        
    def setIdentity(self, text):
        self.identity = text
        
    def setVal(self, val):
        self.times = int(val)
        
        # 這邊沒有寫錯，利用start()呼叫執行緒的run方法
        self.start()
        
    def run(self):
        while self.times > 0 and self.identity:
            # 發射訊號
            self.sinOut.emit(self.identity + "==>" + str(self.times))
            self.times -= 1
            
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_()) # app, main 真正開始執行
    
# 開發程式時經常會執行一些耗時的操作，導致介面停頓，這也就是多執行續派上用場之處--
# 為了解決這個問題，可以建立多個執行緒，利用主執行緒更新介面，再以子執行緒即時處理資料，
# 最後將結果顯示於介面上。
