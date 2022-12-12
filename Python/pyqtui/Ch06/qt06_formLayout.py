# PyQt5 表單佈局
# QFormLayout 是 label-field 形式的表單佈局，意即實現表單方式的佈局。
# 表單是提示使用者進行互動的一種模式，主要由兩行組成，第一行顯示提示訊息給使用者，
# 一般叫做 label 域；第二行要求使用者選擇或輸入，一般叫做 field 域。
# label 與 field 的關係就是 label 關聯 field。
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QTextEdit, QFormLayout)
from PyQt5.QtCore import Qt

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.resize(400, 100)
        self.setWindowTitle("表單佈局管理範例")
        self.initUI()
        
    def initUI(self):
        label1 = QLabel("標題1")
        label2 = QLabel("標題2")
        label3 = QLabel("標題3")
        
        lineEdit1 = QLineEdit()
        lineEdit2 = QLineEdit()
        lineEdit3 = QLineEdit()
        
        formlayout = QFormLayout()
        formlayout.addRow(label1, lineEdit1)
        formlayout.addRow(label2, lineEdit2)
        formlayout.addRow(label3, lineEdit3)
        
        self.setLayout(formlayout)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
    