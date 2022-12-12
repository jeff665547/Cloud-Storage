# PyQt5 進階介面控制項 (容器: 承載更多的控制項)
# QTabWidget的使用
# QTabWidget控制項提供一個標籤頁和一個頁面區域，預設顯示第一個標籤頁的內容，
# 按一下各個標籤頁可以查看對應的頁面。如果一個視窗顯示的輸入欄位很多，
# 建議拆分這些欄位, 再分別放到不同頁面的標籤頁中。
# 在此例中，表單的內容分為三組，每一組的控制項都顯示在不同的標籤頁。
# 頂層視窗是一個QTabWidget控制項，分別加入三個標籤頁進去。
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TabDemo(QTabWidget):
    def __init__(self, parent = None):
        super(TabDemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        
        self.setWindowTitle("Tab example")
        
    # 使用表單佈局管理器，每個標籤頁顯示子表單的內容
    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        self.setTabText(0, "Contact Methods")
        self.tab1.setLayout(layout)
        
    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Boy"))
        sex.addWidget(QRadioButton("Girl"))
        layout.addRow(QLabel("Gender"), sex)
        layout.addRow("Birthday", QLineEdit())
        self.setTabText(1, "Personal details")
        self.tab2.setLayout(layout)
        
    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Subject"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Mathematics"))
        self.setTabText(2, "Education degree")
        self.tab3.setLayout(layout)
        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())
    