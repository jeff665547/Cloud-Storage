# PyQt5 絕對位置佈局
import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui\Ch06")
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        lbl1 = QLabel("Welcome", self)
        lbl1.move(15, 10)   # (0, 0) 為GUI介面的左上角
        
        lbl2 = QLabel("Learning", self)
        lbl2.move(35, 40)
        
        lbl3 = QLabel("PyQt5 !", self)
        lbl3.move(55, 70)
        
        self.setGeometry(300, 300, 320, 120)
        self.setWindowTitle("Example for the absolute position.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec_())