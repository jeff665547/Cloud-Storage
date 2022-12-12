# PyQt5 進階介面控制項 (容器: 承載更多的控制項)
# QStackedWidget的使用
# QStackedWidget是一個堆疊視窗控制項，用來填充一些小控制項，但同時間只會顯示其中一個。
# QStackedWidget 使用 QStackedLayout 佈局，它與QTabWidget類似，
# 可以有效地呈現視窗的控制項。
# e.g. GUI左側的控制面板

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle("StackedWidget Example")
        
        # 每個子控制項都能擁有自己的佈局，包含特定的表單元素。
        # 不能在頁面之間切換QStackedWidget，它連結至目前選中QListWidget控制項的選項。
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, "Contact Methods")
        self.leftlist.insertItem(1, "Personal Info")
        self.leftlist.insertItem(2, "Education Degree")
        self.leftlist.currentRowChanged.connect(self.display)
        
        self.stack1 = tt()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        
        # QStackedWidget物件填入三個子控制項
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist) # 左邊是list
        hbox.addWidget(self.Stack)    # 右邊是StackedWidget
        
        self.setLayout(hbox)
        
    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        self.stack1.setLayout(layout)
    
    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Boy"))
        sex.addWidget(QRadioButton("Girl"))
        layout.addRow(QLabel("Gender"), sex)
        layout.addRow("Birthday", QLineEdit())
        self.stack2.setLayout(layout)
        
    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Subject"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Mathematics"))
        self.stack3.setLayout(layout)
        
    def display(self, i):
        # 將QListWidget的currentRowChanged訊號與display()槽函數相關聯，
        # 進而改變堆疊控制項的視圖。
        self.Stack.setCurrentIndex(i)
        
    
class tt(QWidget):
    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0.3)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))   
        painter.drawRect(self.rect())
        
        
        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())
