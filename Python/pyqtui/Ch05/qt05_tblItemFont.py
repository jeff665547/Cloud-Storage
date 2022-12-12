# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 2. 設定儲存格
# 將字體加粗
# 在此例中，我們將新表格第一列中三個儲存格的文字都設成粗體。

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )
from PyQt5.QtGui import (QBrush, QColor, QFont)

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
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['Name','Gender','Weight(kg)'])

        newItem = QTableWidgetItem("John")
        newItem.setFont(QFont("Times", 12, QFont.Black))
        tableWidget.setItem(0, 0, newItem)  

        newItem = QTableWidgetItem("boy")
        newItem.setFont(QFont("Times", 12, QFont.Black))
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("160")
        newItem.setFont(QFont("Times", 12, QFont.Black))
        tableWidget.setItem(0, 2, newItem)     

        self.setLayout(conLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())