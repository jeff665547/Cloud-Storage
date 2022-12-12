# PyQt5 QSplitter 自由彈性邊界管理
# 除了 Layout 佈局管理以外，PyQt還有一個特殊的佈局管理器QSplitter。
# QSplitter 允許拖動子控制項的邊界控制其大小，並提供一個處理拖曳子控制項的控制器。
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SplitterExample(QWidget):
    def __init__(self, parent = None):
        super(SplitterExample, self).__init__(parent)
        self.setWindowTitle("QSplitter Example")
        self.setGeometry(300, 300, 300, 200)
        self.initUI()
        
    def initUI(self):
        hbox = QHBoxLayout(self)
        
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        
        textedit = QTextEdit()
        
        # 第一個 QSplitter 物件包含一個 QFrame 物件和 QTextEdit 物件，
        # 並按照水平方向佈局。
        # 設定水平佈局方向。
        splitter1 = QSplitter(Qt.Horizontal)
        
        # 將小控制項加到QSplitter管理器的佈局中。
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        
        # 設定控制項的初始化大小。
        splitter1.setSizes([100, 200]) 
        
        
        # 第二個 QSplitter 物件包含第一個 QSplitter 物件和另一個 QFrame 物件，
        # 並按照垂直方向佈局。
        # 設定垂直佈局方向。
        splitter2 = QSplitter(Qt.Vertical)
        
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        
        
        
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = SplitterExample()
    demo.show()
    sys.exit(app.exec_())
    