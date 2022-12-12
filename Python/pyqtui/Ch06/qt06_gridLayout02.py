# PyQt5 格子佈局(跨越行和列的儲存格)
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QTextEdit, QGridLayout)
from PyQt5.QtCore import Qt

class Winform(QWidget):
    def __init__(self, parent = None):
        super(Winform, self).__init__(parent)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("故障申告")
        self.initUI()
        
    def initUI(self):
        title = QLabel("標題")
        author = QLabel("提交人")
        review = QLabel("申告內容")
        
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        # 把 title 放在 QGridLayout佈局的第1列第0行
        grid.addWidget(title, 1, 0)
        # 把 titleEdit 放在 QGridLayout佈局的第1列第1行
        grid.addWidget(titleEdit, 1, 1)
        
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        
        # 把 review 放在 QGridLayout佈局的第3列第0行
        grid.addWidget(review, 3, 0)
        # 把 reviewEdit 放在 QGridLayout佈局的第3列第1行，並且占用共5列和1行
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid)
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = Winform()
    demo.show()
    sys.exit(app.exec_())
    