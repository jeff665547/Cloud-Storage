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
# 本例示範訊號與槽的機制完成不同的視窗之間傳遞參數。
# 對於多視窗的資料傳遞，一般是透過子視窗發射訊號，由主視窗透過槽函數捕捉此訊號，
# 然後取得其內的資料。子視窗發射的訊號有兩種，第一種是發射PyQt內建的訊號；
# 另一種是發射自訂的訊號。本例將介紹這兩種方式的訊號與槽機制。
#
# 自訂訊號的好處是：可以自訂它的參數類型。當發射一個自訂訊號時，參數類型可以是
# int, str, dict, list等； 如果發射內建訊號，則只能是幾個特定的參數。
#
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch07")
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog2 import DateDialog

class WinForm(QWidget):
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle("訊號與槽傳遞參數的範例")
        
        self.open_btn = QPushButton("取得時間")
        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_emit = QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)
        
        self.lineEdit_inner.setText("接收子視窗內建訊號的時間")
        self.lineEdit_emit.setText("接收子視窗自訂訊號的時間")
        
        grid = QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)
        
        grid.addWidget(self.open_btn)
        self.setLayout(grid)
        
    def openDialog(self):
        dialog = DateDialog(self)
        
        # 對於主視窗來說，關鍵是取得子視窗的訊號，並且連結到自己的槽函數，
        # 這樣就完成了子視窗的控制項與主視窗的控制項，其間訊號與槽的繫結。
        """連結子視窗的內建訊號與主視窗的槽函數"""
        dialog.datetime_inner.dateTimeChanged.connect(
            self.deal_inner_slot)
        # 每當子視窗控制項datetime_inner的時間發生變化時，就會觸發主視窗的槽函數
        # deal_inner_slot去撈子視窗的日期。        
        
        """連結子視窗的自訂訊號與主視窗的槽變數"""
        dialog.Signal_OneParameter.connect(self.deal_emit_slot) 
        # 每當子視窗的Signal_OneParameter發生變化時(按下OK按鈕時)才會觸發主視窗
        # 的槽函數deal_emit_slot來接收子視窗發射出來的日期資料。
        
        dialog.show()
        
    def deal_inner_slot(self, date):
        self.lineEdit_inner.setText(date.toString())
        
    def deal_emit_slot(self, dateStr):
        self.lineEdit_emit.setText(dateStr)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())