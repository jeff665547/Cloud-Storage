# PyQt5 進階介面控制項 (容器: 承載更多的控制項)
# QScrollBar 的使用
# QScrollBar 即為　GUI　邊邊的捲軸
# QScrollBar 為視窗控制項提供水平或垂直的捲軸，藉以擴大目前視窗的有效裝載面積，
# 進而呈現更多的控制項。
# 此例展示如何在PyQt5的視窗使用QScrollbar控制項。
# 利用三個滑動條來便利地控制標籤文字字體顏色的RGB值。
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QHBoxLayout()
        self.ll = QLabel("Move the scroll bar to change color.")
        self.ll.setFont(QFont("Arial", 16))
        hbox.addWidget(self.ll)
        self.s1 = QScrollBar()
        self.s1.setMaximum(255)
        # 當拖曳滑塊時，便連接sliderMoved訊號與槽函數sliderval()。
        self.s1.sliderMoved.connect(self.sliderval)
        self.s2 = QScrollBar()
        self.s2.setMaximum(255)
        # 當拖曳滑塊時，便連接sliderMoved訊號與槽函數sliderval()。
        self.s2.sliderMoved.connect(self.sliderval)
        self.s3 = QScrollBar()
        self.s3.setMaximum(255)
        # 當拖曳滑塊時，便連接sliderMoved訊號與槽函數sliderval()。
        self.s3.sliderMoved.connect(self.sliderval)
        hbox.addWidget(self.s1)
        hbox.addWidget(self.s2)
        hbox.addWidget(self.s3)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QScrollBar Example")
        self.setLayout(hbox)
        
    def sliderval(self):
        print(self.s1.value(), self.s2.value(), self.s3.value())
        palette = QPalette()
        c = QColor(self.s1.value(), self.s2.value(), self.s3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.ll.setPalette(palette)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec_())
