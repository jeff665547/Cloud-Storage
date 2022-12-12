# PyQt5 訊號與槽
# 根據訊號與槽的性質進行分類
# 2. 內建訊號和自訂槽函數
from PyQt5.QtWidgets import *
import sys

# 展示點擊按鈕時關閉視窗，並使用內建的訊號和自訂的槽函數
class Winform(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle("內建的訊號和自訂的槽函數範例")
        self.resize(330, 50)
        self.initUI()
        
    def initUI(self):
        
        btn = QPushButton("Close", self)
        # button 不透過 layout 的方式直接加入 GUI 介面裏頭的寫法
        # 這邊的 self 指Winform類的實體，在此例中是win
        
        btn.clicked.connect(self.btn_close)
        
    def btn_close(self):
        # 自訂槽函數
        self.close()        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())

# 按下Close後，觸發按鈕內建的訊號(clicked)，
# 然後連結自訂的槽函數(self.btn_close)
