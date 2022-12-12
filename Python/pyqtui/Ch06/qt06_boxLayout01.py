# PyQt5 水平佈局
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, \
QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("水平佈局管理範例")
        
        # 水平佈局按照從左到右的順序增加按鈕控制項
        hlayout = QHBoxLayout() # 初始化水平佈局
        
        # 增加Button元件
        hlayout.addWidget( QPushButton("1") )
        hlayout.addWidget( QPushButton("2") )
        hlayout.addWidget( QPushButton("3") )        
        hlayout.addWidget( QPushButton("4") )
        hlayout.addWidget( QPushButton("5") )
        
        # 設定控制項間距
        hlayout.setSpacing(0)
        
        # 應用到當前的Layout
        self.setLayout(hlayout)  
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
    