# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 2. 設定儲存格
# 表格中不顯示分隔線
# 在此例中，展示如何將表格中的格線隱藏起來

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtGui import (QBrush, QColor, QFont)
from PyQt5.QtCore import Qt

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

        tableWidget.setHorizontalHeaderLabels(['Name','Gender','Height(cm)'])
        tableWidget.setShowGrid(False) # 關閉格線的顯示
        
        newItem = QTableWidgetItem("John")
        tableWidget.setItem(0, 0, newItem)  

        newItem = QTableWidgetItem("boy")
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("170")
        tableWidget.setItem(0, 2, newItem)     
        
        
        self.setLayout(conLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())