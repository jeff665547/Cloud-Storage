# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 1. 基本用法
# QTableWidget是Qt程式常用來顯示資料表格的類別(呈現方式為表格模式)，類似C#的DataGrid。
# QTableWidget是QTableView的子類別，它使用標準的資料模型，
# 並且其儲存格資料是透過QTableWidgetItem物件達成。
# 使用QTableWidget時就需要QTableWidgetItem類別，藉以呈現表格中的儲存格。
# 整個表格便是以各個儲存格建構而成。
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication,
                             QTableWidgetItem, QHeaderView, QComboBox, QPushButton)
from PyQt5.QtCore import Qt
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
        
        # 在儲存格中置放控制項
        # QTableWidget不僅允許在儲存格置放文字，還能夠置放控制項，
        # 方式是透過TableWidget.setItem()增加PyQt的基本控制項
        # 將下拉式清單方塊加入儲存格中
        comBox = QComboBox()
        comBox.addItem("Boy")
        comBox.addItem("Girl")
        comBox.setStyleSheet("QComboBox(margin:3px);") # 設定控制項與儲存格的邊距(3像素)
        tableWidget.setCellWidget(0, 1, comBox)
        
        # 將按鈕加入儲存格中
        searchBtn = QPushButton("Fix")
        searchBtn.setDown(True)
        searchBtn.setStyleSheet("QPushButton(margin:3px);") # 設定控制項與儲存格的邊距(3像素)
        tableWidget.setCellWidget(0, 2, searchBtn)
        
        
        self.setLayout(conLayout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())


