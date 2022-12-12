# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 1. 基本用法
# QTableWidget是Qt程式常用來顯示資料表格的類別(呈現方式為表格模式)，類似C#的DataGrid。
# QTableWidget是QTableView的子類別，它使用標準的資料模型，
# 並且其儲存格資料是透過QTableWidgetItem物件達成。
# 使用QTableWidget時就需要QTableWidgetItem類別，藉以呈現表格中的儲存格。
# 整個表格便是以各個儲存格建構而成。
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import (QColor, QBrush)

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QTableWidget Example")
        self.resize(600, 800)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(30)
        tableWidget.setColumnCount(4)
        conLayout.addWidget(tableWidget)
        
        for i in range(30):
            for j in range(4):
                itemContent = "({}, {})".format(i, j)
                tableWidget.setItem(i, j, QTableWidgetItem( itemContent ))
                
        self.setLayout(conLayout)
        
        # 在表格中快速定位到指定列 (需另外寫function，在此僅列出做參考，不會work)
        # 當tableWidget表格有很多列時，可以透過輸入列號直接定位與顯示，例如輸入10，
        # 就直接顯示第10列。
        # 巡訪表格找尋對應的項目
        text = "(10, 1)"
        items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)
        item = items[0]
        # 選中儲存格(儲存格反白)
        item.setSelected(True)
        # 設定儲存格的背景顏色(文字顏色)為紅色
        item.setForeground(QBrush(QColor(255, 0, 0)))
        
        # 取得列號
        row = item.row()
        # 模擬透過滑鼠滾輪，快速定位到第11列
        tableWidget.verticalScrollBar().setSliderPosition(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
