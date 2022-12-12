# PyQt5 格子佈局(單一儲存格)
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QHBoxLayout, 
                             QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("格子佈局管理範例")
        self.move(300, 150)
        self.initUI()
        
    def initUI(self):
        # 1 建立QGridLayout實例，並設為視窗的佈局
        grid = QGridLayout()
        self.setLayout(grid)
        
        # 2 建立按鈕的標籤列表
        names = ["Cls", "Back", "", "Close", 
                 "7", "8", "9", "/", 
                 "4", "5", "6", "*",
                 "1", "2", "3", "-", 
                 "0", "-", "=", "+"]
        
        # 3 在格子中建立一個位置列表
        positions = [(i, j) for i in range(5) for j in range(4)]
        
        # 4 建立按鈕，並透過addWidget() 方法加到佈局中
        for position, name in zip(positions, names):
            if name == "":
                continue
            
            button = QPushButton(name)
            grid.addWidget(button, *position)
            # grid.addWidget(QWidget widget, int row, int col,
            #                int alignment = 0)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
    
