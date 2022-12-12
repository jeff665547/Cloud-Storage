import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstMainWin import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    # Ui_MainWindow is in the firstMainWin.py
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
