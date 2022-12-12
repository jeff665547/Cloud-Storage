# PyQt5 巢狀佈局
# 在視窗完成單一佈局並不難，但若打算設計比較複雜的佈局時，就涉及巢壯式的佈局了，
# 此時建議以 Qt Designer 的視覺化管理工具進行介面佈局。
# 在此例中，有多少種局部佈局，就需要多少個空白控制項
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout, 
                             QVBoxLayout, QGridLayout, QFormLayout, QPushButton)
from PyQt5.QtCore import Qt

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.resize(400, 100)
        self.setWindowTitle("巢狀佈局範例")
        self.initUI()
        
    def initUI(self):
        # 初始化全域佈局(1種): 水平佈局
        wlayout = QHBoxLayout()
        
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
        
        # 準備(初始化)4個控制項
        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()
        
        # 4個控制項設定局部佈局
        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(formlayout)
        
        # 將4個控制項加到全域佈局中
        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)
        
        # 將視窗本身設為全域佈局
        self.setLayout(wlayout)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
    