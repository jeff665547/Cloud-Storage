# PyQt5 進階介面控制項 (容器: 承載更多的控制項)
# QDockWidget的使用
# QDockWidget是一個停靠在QMainWindow內的視窗控制項，它保持在浮動的狀態，
# 或者於指定位置作為子視窗附加到主視窗。
# QMainWindow 類別的主視窗物件，保有一個用來停靠視窗的區域，此區域位於控制項的中央周圍。

import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DockDemo(QMainWindow):
    def __init__(self, parent = None):
        super(DockDemo, self).__init__(parent)
        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")
        file.addAction("Quit")
        
        # 建立可停靠的視窗items
        self.items = QDockWidget("Dockable", self)
        
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        
        # 在停靠視窗items內加入QListWidget物件
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        
        # 頂層視窗是一個QMainWindow物件(繼承自QMainWindow)，
        # QTextEdit物件是它的中央小控制項
        self.setCentralWidget(QTextEdit())
        # 將停靠視窗放在中央小控制項的右側
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        
        self.setWindowTitle("Dock Example")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())
    