# PyQt5 訊號與槽
# 訊號與槽有三種使用方法:
# 1. 內建訊號與槽的使用
# 2. 自訂訊號與槽的使用
# 3. 裝飾器訊號與槽的使用 (為第1種方法的衍伸)
#
# 本例接續介紹第三類方法: 裝飾器訊號與槽的使用以及其他訊號與槽的進階用法，
# 重點將放在使用自訂參數以及自訂參數的傳遞。
# Remark: 訊號發出的參數個數一定要大於槽函數接收的參數個數。
# 
# 解決辦法: 使用lambda運算式
# lambda 運算式除了傳遞按鈕數字給槽函數之外，也可以傳送其他東西，
# 甚至是按鈕控制項本身(如，槽函數打算把按鈕改為不可用的情況)
import sys
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QWidget, QMessageBox, 
                             QApplication, QHBoxLayout)

class WinForm(QMainWindow):
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        
        # 使用lambda運算式解決訊號發出的參數個數小於槽函數接收的參數個數問題
        btn1.clicked.connect(lambda: self.onButtonClick(1))
        btn2.clicked.connect(lambda: self.onButtonClick(2))
        
        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
        
    def onButtonClick(self, n):
        print("Button {} 被按下了".format(n))
        QMessageBox.information(self, "訊息提示框", "Button {} clicked!".format(n))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
    