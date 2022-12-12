# PyQt5 垂直佈局
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, \
QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("垂直佈局管理範例")
        
        # 垂直佈局按照從上到下的順序增加按鈕控制項
        vlayout = QVBoxLayout() # 初始化水平佈局
        
        # 增加Button元件
        vlayout.addWidget( QPushButton("1") )
        vlayout.addWidget( QPushButton("2") )
        vlayout.addWidget( QPushButton("3") )        
        vlayout.addWidget( QPushButton("4") )
        vlayout.addWidget( QPushButton("5") )
        
        # 應用到當前的Layout
        self.setLayout(vlayout)  
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
    