# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 2. 設定儲存格
# 改變儲存格顯示的圖片大小 & 取得儲存格的內容
# 在此例中，在每個儲存格中擺放圖片，甚至改變圖片的大小
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
        self.resize(900, 1000);
        conLayout = QHBoxLayout()
        
        table = QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(5)
        
        table.setHorizontalHeaderLabels(["Image 1", "Image 2", "Image 3"])
        
        table.setEditTriggers( QAbstractItemView.NoEditTriggers )
        table.setIconSize(QSize(200, 300));
        
        for i in range(3):   # 讓行寬和圖片相同
            table.setColumnWidth(i, 200)
        
        for i in range(5):   # 讓列高和圖片相同
            table.setRowHeight(i, 300)
        
        for k in range(15):  # 模擬產生15筆紀錄
            i = k//3
            j = k%3
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled)   # 使用者點擊表格時，便選中圖片
            icon = QIcon("./games{}".format(k))
            item.setIcon(QIcon(icon))
            item.setText("Games ({}, {})".format(i + 1, j + 1))
            
            print("{}.png i = {} j = {}".format(k, i, j))
            table.setItem(i, j, item)
        
        conLayout.addWidget(table)
        self.setLayout(conLayout)
        
        # 取得儲存格的內容
        table.itemClicked.connect( self.getItem )
    
    def getItem(self, item):
        
        print("You selected => " + item.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())