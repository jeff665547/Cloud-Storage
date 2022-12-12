# PyQt5 圖形與特效
# 設定樣式
# 為指定按鈕加上背景圖片(指定特定的QPushButton)
# 
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch08")

from  PyQt5.QtWidgets import (QApplication, QLabel, QWidget, 
                              QVBoxLayout, QPushButton)
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        #1
        label1 = QLabel(self)
        label1.setToolTip("這是一個文字標籤")
        label1.setStyleSheet("QLabel{border-image: url(./image1.jpg)}")
        label1.setText("This is a text label, and it has a background!")
        # 設定標籤的寬度和高度
        label1.setFixedWidth(476)
        label1.setFixedHeight(259)

        #2
        btn1 = QPushButton(self)
        btn1.setObjectName("btn1")  # 為指定按鈕加上背景圖片時需要呼叫這一行指令，
                                    # 為按鈕物件設定一個名稱。
        btn1.setMaximumSize(64, 64)
        btn1.setMinimumSize(64, 64)
        # left.png與lefthover.png的尺寸是一樣的
        style = """
                    #btn1{
                        border-radius: 30px;
                        background-image: url("./left.png");
                        }
                    #btn1:hover{
                        border-radius: 30px;
                        background-image: url("./lefthover.png");
                        }
                    #btn1:Pressed{
                        border-radius: 30px;
                        background-image: url("./leftPressed.png");
                        }
                """
        btn1.setStyleSheet(style)
        
        #3
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(btn1)
        
        self.setLayout(vbox)
        self.setWindowTitle("按鈕和Label添加背景圖片例子")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())