# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 1. 基本用法
# QTableWidget是Qt程式常用來顯示資料表格的類別(呈現方式為表格模式)，類似C#的DataGrid。
# QTableWidget是QTableView的子類別，它使用標準的資料模型，
# 並且其儲存格資料是透過QTableWidgetItem物件達成。
# 使用QTableWidget時就需要QTableWidgetItem類別，藉以呈現表格中的儲存格。
# 整個表格便是以各個儲存格建構而成。
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication,
                             QTableWidgetItem, QHeaderView, QAbstractItemView)
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
        tableWidget = QTableWidget() # 先初始化表格(初始化行數和列數)
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)
        
        # 設定表格的水平表頭標籤和垂直表頭標籤(header)
        tableWidget.setHorizontalHeaderLabels(["Name", "Gender", "Weight (kg)"])
        tableWidget.setVerticalHeaderLabels([' row 1', ' row 2', ' row 3', ' row 4'])
        
        # 設定表格表頭為伸縮模式
        # 使用QTableWidget物件的horizontalHeader()函數，
        # 將表格設定為自我調整的伸縮模式，意即可根據視窗大小改變格子大小
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # 產生一個QTableWidgetItem物件，名稱為John        
        newItem = QTableWidgetItem("John")
        # 將剛才產生的具體儲存格，載入表格的第0列第0行處。
        tableWidget.setItem(0, 0, newItem)
        
        newItem = QTableWidgetItem("Boy")
        tableWidget.setItem(0, 1, newItem)
        
        newItem = QTableWidgetItem("160")
        tableWidget.setItem(0, 2, newItem)
        
        # 將表格變為禁止編輯
        # 在預設情況下，可以更改表格中的字串，例如按兩下儲存格，就能修改原先的內容。
        # 想禁止這種操作，將表格設成唯讀即可。 (需import QAbstractItemView)
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # 設定表格整列選中
        # 表格預設選中的是單個儲存格，現在改成點選後直接整列反白
        tableWidget.setSelectionBehavior(tableWidget.SelectRows)
        
        # 將行和列的寬度、高度，設定為與顯示內容的寬度、高度相互配合 
        # (名稱長的內容給予較寬(高)的格子)
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()
        
        # 顯示與隱藏表頭(header)
        # 垂直方向(每個row名稱)
        tableWidget.verticalHeader().setVisible(False)
        
        # 顯示與隱藏表頭(header)
        # 水平方向(每個column名稱)
        tableWidget.horizontalHeader().setVisible(True)
        
        self.setLayout(conLayout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())