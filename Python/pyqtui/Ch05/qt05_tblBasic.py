# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 1. 基本用法
# QTableWidget是Qt程式常用來顯示資料表格的類別(呈現方式為表格模式)，類似C#的DataGrid。
# QTableWidget是QTableView的子類別，它使用標準的資料模型，
# 並且其儲存格資料是透過QTableWidgetItem物件達成。
# 使用QTableWidget時就需要QTableWidgetItem類別，藉以呈現表格中的儲存格。
# 整個表格便是以各個儲存格建構而成。
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication,
                             QTableWidgetItem)
import sys

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QTableWidget Example")
        self.resize(400, 300);
        conLayout = QHBoxLayout()
        # 建構一個QTableWidget物件,並且設定表格為4列3行
        tableWidget = QTableWidget() # 或直接下 QTableWidget(4, 3) 意思等價
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)
        
        # 設定表格的表頭(header)
        tableWidget.setHorizontalHeaderLabels(["Name", "Gender", "Weight (kg)"])
        
        # 產生一個QTableWidgetItem物件，名稱為John        
        newItem = QTableWidgetItem("John")
        # 將剛才產生的具體儲存格，載入表格的第0列第0行處。
        tableWidget.setItem(0, 0, newItem)
        
        mewItem = QTableWidgetItem("Boy")
        tableWidget.setItem(0, 1, newItem)
        
        newItem = QTableWidgetItem("160")
        tableWidget.setItem(0, 2, newItem)
        
        self.setLayout(conLayout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())