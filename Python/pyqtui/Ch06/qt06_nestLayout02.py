# PyQt5 巢狀佈局
# 與 qt06_nestLayout01.py 不同。在此例中，有多少種局部佈局，只需要一個空白控制項。
import os
import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self, parent = None):
        super(MyWindow, self).__init__(parent)
        self.resize(700, 200)
        self.setWindowTitle("巢狀佈局範例")
        self.initUI()
        
    def initUI(self):
        
        # 準備全域控制項(注意參數self)，用來「乘載」全域佈局
        wwg = QWidget(self)
        
        # 定義全域佈局(注意參數wwg)
        wl = QHBoxLayout(wwg)
        
        # 初始化局部佈局(4種): 水平佈局、垂直佈局、格子佈局、表單佈局
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        formlayout = QFormLayout()
        
        # 生成局部佈局的控制項(例如: 按鈕)
        # hlayout
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        # vlayout
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")
        # glayout
        btn5 = QPushButton("5")
        btn6 = QPushButton("6")
        btn7 = QPushButton("7")
        btn8 = QPushButton("8")
        # formlayout
        btn9 = QPushButton("9")
        btn10 = QPushButton("10")
        btn11 = QPushButton("11")
        btn12 = QPushButton("12")
        
        # 為局部佈局增加控制項(例如: 按鈕)
        hlayout.addWidget( btn1 )
        hlayout.addWidget( btn2 )
        vlayout.addWidget( btn3 )
        vlayout.addWidget( btn4 )
        glayout.addWidget( btn5 , 0, 0)
        glayout.addWidget( btn6 , 0, 1)
        glayout.addWidget( btn7 , 1, 0)
        glayout.addWidget( btn8 , 1, 1)
        formlayout.addWidget( btn9 )
        formlayout.addWidget( btn10 )
        formlayout.addWidget( btn11 )
        formlayout.addWidget( btn12 )
        
        # 把4 種局部佈局增加到全域佈局中
        wl.addLayout(hlayout)
        wl.addLayout(vlayout)
        wl.addLayout(glayout)
        wl.addLayout(formlayout)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = MyWindow()
    demo.show()
    sys.exit(app.exec_())
    