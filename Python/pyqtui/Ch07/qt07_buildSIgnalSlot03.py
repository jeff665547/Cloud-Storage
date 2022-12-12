# PyQt5 訊號與槽
# 根據訊號與槽的性質進行分類
# 3. 自訂訊號和內建槽函數
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

# 展示點擊按鈕時關閉視窗，並使用自訂的訊號和內建的槽函數
class Winform(QWidget):
    
    # 自訂訊號，不帶參數
    button_clicked_signal = pyqtSignal()
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle("自訂的訊號和內建的槽函數範例")
        self.resize(330, 50)
        self.initUI()
        
    def initUI(self):

        btn = QPushButton("Close", self)
        
        # 連接訊號與槽函數(第一層)
        btn.clicked.connect(self.btn_clicked)
        
        # 接收訊號，連接到槽函數(第二層)
        self.button_clicked_signal.connect(self.close)
        
    def btn_clicked(self):
        # 發送自訂訊號，無參數(emit 傳遞參數給已經連接的槽函數)
        self.button_clicked_signal.emit()
        # 這邊後面不能直接接conect.close 因為需要emit來發射訊號
        # 要使用connect()就要有emit()還有pyqtSignal。
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())

# 按下Close後，觸發按鈕自訂的訊號(button_clicked_signal)，
# 然後連結視窗(QWidget)內建的槽函數(self.close)
