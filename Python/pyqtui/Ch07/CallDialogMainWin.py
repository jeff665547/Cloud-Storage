# PyQt5 訊號與槽
# 傳遞視窗資料
# 開發程式時，若程式只有一個視窗，只需關心視窗裡面各個控制項之間如何傳遞資料
# 但在設計PyQt程式的過程中，經常會遇到輸入或選擇多個參數的問題。
# 若將多個參數寫到一個視窗，主視窗會顯得很臃腫。因此，
# 一般是加入一個按鈕然後調用對話方塊，接著在對話方塊挑選參數，
# 當關閉對話方塊時再將參數值返回主視窗。
#
# 為此，PyQt提供一些標準的對話方塊類別，應用於輸入資料、修改資料、更改應用程式的設定等，
# 常見的有QFileDialog, QInputDialog, QColorDialog, QFontDialog等。
#
# 在不同的視窗之間傳遞參數，一般有兩種解決辦法。
# 1. 由主視窗取得子視窗控制項的屬性(即在自訂對話方塊之間透過屬性傳遞)
# 2. 透過訊號與槽機制，子視窗以發射訊號的形式傳遞資料，
#    再由主視窗的槽函數接收這些資料。(即在視窗之間以訊號與槽的機制完成)
#
# 本例示範調用屬性來傳遞多個視窗資料(即由主視窗取得子視窗控制項的屬性)
# 在主視窗調用對話方塊有兩種方式，此兩種方法最後呈現的結果一模一樣
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch07")
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog import DateDialog

class WinForm(QWidget):
    
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle("關閉對話方塊時，返回值給主視窗範例")
        
        self.lineEdit = QLineEdit(self)
        
        self.button1 = QPushButton("彈出對話方塊1")
        self.button1.clicked.connect(self.onButton1Click)
        
        self.button2 = QPushButton("彈出對話方塊2")
        self.button2.clicked.connect(self.onButton2Click)
        
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)
        
    # 第一種方法：直接在主視窗產生對話方塊物件，然後呼叫其函數取得返回值
    #           再根據對話方塊的返回值(按確認或取消鈕)進行下一步操作。
    def onButton1Click(self):
        dialog = DateDialog(self)  # 直接在主視窗產生對話方塊物件
        result = dialog.exec_()    
        date = dialog.dateTime()   # 呼叫其函數取得返回值(傳遞子視窗資料)
        
        # 顯示到主視窗的Line Editor
        self.lineEdit.setText(date.date().toString() + "Main Window")
        print("\n 日期對話方塊的返回值")
        print("date = {}".format(str(date.date())))
        print("time = {}".format(str(date.time())))
        print("result = {}".format(result))
        dialog.destroy()
        
    # 第二種方法：在主視窗呼叫子視窗的靜態函數，利用靜態函數的特點，
    # 在子視窗的靜態函數產生實例物件。
    def onButton2Click(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print("\n 日期對話方塊的返回值")
        print("date = {}".format(str(date)))
        print("time = {}".format(str(time)))
        print("result = {}".format(result))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())