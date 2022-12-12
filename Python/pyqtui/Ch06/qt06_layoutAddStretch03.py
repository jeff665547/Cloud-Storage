# PyQt5 addStretch()
# stretch: (按鈕間的伸縮量)  扣除widgets後，按比例分配剩餘空間。
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
                             QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt

class WindowDemo(QWidget):
    def __init__(self, parent = None):
        super(WindowDemo, self).__init__(parent)
        self.setWindowTitle("addStretch()範例")
        
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")
        btn5 = QPushButton("5")
        
        # Initialization
        hlayout = QHBoxLayout()
        
        # 在最後一個控制項(widget)後設定伸縮控制，好讓所有控制項都靠左顯示
        
        hlayout.addWidget( btn1 )
        hlayout.addWidget( btn2 )
        hlayout.addWidget( btn3 )
        hlayout.addWidget( btn4 )
        hlayout.addWidget( btn5 )
        
        # 設定伸縮控制
        hlayout.addStretch(0)  # 預設值為0

        
        # 應用到當前的Layout
        self.setLayout(hlayout)  
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = WindowDemo()
    demo.show()
    sys.exit(app.exec_())
    