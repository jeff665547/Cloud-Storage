# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 2. 設定儲存格
# 為儲存格增加圖片
# 在此例中，在儲存格內增加圖片，並顯示圖片的描述資訊
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

os.chdir("C:/Users/jeff/Desktop/pyqtui/Ch05")

class Table(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget Example")
        self.resize(430,230);

        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(4)
        conLayout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(["Name", "Nick Name", "Price(NTD)", "Image"])
        tableWidget.setShowGrid(False) # 關閉格線的顯示

        newItem = QTableWidgetItem("Need for Speed")
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("NFS")
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("980")
        tableWidget.setItem(0, 2, newItem)

        newItem = QTableWidgetItem(QIcon("games5.jpg"), "Need for speed")
        tableWidget.setItem(0, 3, newItem)

        self.setLayout(conLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())