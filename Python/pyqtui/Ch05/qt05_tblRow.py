# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 2. 設定儲存格
# 設定儲存格的大小
# 在此例中，展示如何將第二行的儲存格寬度設為1500，第一列的儲存格高度設為120
import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )
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
        tableWidget.setSpan(0, 0, 3, 1) 
        # 原本占據一列一行的第一列第一行儲存格改為佔據三列一行
        
        newItem = QTableWidgetItem("John")
        tableWidget.setItem(0, 0, newItem)  
        newItem.setTextAlignment( Qt.AlignRight | Qt.AlignBottom ) 
        # 靠右對齊並與底部對齊

        newItem = QTableWidgetItem("boy")
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("170")
        tableWidget.setItem(0, 2, newItem)     
        
        tableWidget.setColumnWidth(1, 1500)
        tableWidget.setRowHeight(0, 120)
        
        
        self.setLayout(conLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())