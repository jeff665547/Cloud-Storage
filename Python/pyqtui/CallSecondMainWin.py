import os
os.chdir(r"C:\Users\jeff\Desktop\pyqtui")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from secondMainWin import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    # Ui_MainWindow is in the secondMainWin.py
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkBox.setChecked(True)
        # 功能表的點擊事件，當點擊關閉功能表時連接槽函數 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 功能表的點擊事件，當點擊開啟功能表時連接槽函數 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)
        
    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "開啟", "C:/", "All Files (*);; Text Files (*.txt)")
        self.statusbar.showMessage(file)
        
    def on_checkBox_clicked(self, checked):
        self.label.setVisible(checked)
        self.label.setEnabled(checked)
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
