# PyQt5 addStretch()
# stretch: (按鈕間的伸縮量)  扣除widgets後，按比例分配剩餘空間。
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, \
QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class WindowDemo(QWidget):
    def __init__(self, parent = None):
        super(WindowDemo, self).__init__(parent)
        self.setWindowTitle("addStretch()範例")
        
        btn1 = QPushButton("button 1")
        btn2 = QPushButton("button 2")
        btn3 = QPushButton("button 3")
        
        # Initialization
        hbox = QHBoxLayout()
        
        # 將按鈕以外的空白區域均等份為4份
        # 並依照指定的順序放入按鈕的佈局管理器中
        # 每個控制項間都增加了伸縮量，所有控制項之間的間距都一樣
        
        # 設定伸縮量為1
        hbox.addStretch(1)
        hbox.addWidget( btn1 )
        # 設定伸縮量為1
        hbox.addStretch(1)
        hbox.addWidget( btn2 )
        # 設定伸縮量為1
        hbox.addStretch(1)
        hbox.addWidget( btn3 )
        # 設定伸縮量為1
        hbox.addStretch(1)
        
        # 應用到當前的Layout
        self.setLayout(hbox)  
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = WindowDemo()
    demo.show()
    sys.exit(app.exec_())
    
