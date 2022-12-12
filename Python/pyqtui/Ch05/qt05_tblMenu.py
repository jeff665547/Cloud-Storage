# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 3. 支援右鍵選單
# 在此例中, 選中某個儲存格後，按一下滑鼠右鍵，從彈出的快顯功能表挑選
# "Option 1", "Option 2", "Option 3", 後台的輸出結果為:
#  You chose the option 2, the context is John Boy 160.
import sys
from PyQt5.QtWidgets import (QMenu, QPushButton, QWidget, QTableWidget, 
                             QHBoxLayout, QApplication, QDesktopWidget,
                             QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot


class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QTableWidget demo")
        self.resize(500, 300)
        conLayout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        conLayout.addWidget(self.tableWidget)
        
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Gender", "Weight"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        newItem = QTableWidgetItem("John")
        self.tableWidget.setItem(0, 0, newItem)
        
        newItem = QTableWidgetItem("Boy")
        self.tableWidget.setItem(0, 1, newItem)
        
        newItem = QTableWidgetItem("160")
        self.tableWidget.setItem(0, 2, newItem)
        
        newItem = QTableWidgetItem("Alice")
        self.tableWidget.setItem(1, 0, newItem)
        
        newItem = QTableWidgetItem("Girl")
        self.tableWidget.setItem(1, 1, newItem)
        
        newItem = QTableWidgetItem("170")
        self.tableWidget.setItem(1, 2, newItem)
        
        # 允許右鍵產生選單
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 將右鍵選單繫結到槽函數 generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        self.setLayout(conLayout)
        
    def generateMenu(self, pos):
        
        row_num = -1
        
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
            
        # 表格中只有兩筆有效資料，所以只在前兩列支援右鍵彈出選單
        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction(u"Option 1") # 增加右鍵清單裡面的選單
            item2 = menu.addAction(u"Option 2") # 增加右鍵清單裡面的選單
            item3 = menu.addAction(u"Option 3") # 增加右鍵清單裡面的選單
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            
            if action == item1:
                print("You chose the option 1, the context is", 
                      self.tableWidget.item(row_num, 0).text(), 
                      self.tableWidget.item(row_num, 1).text(), 
                      self.tableWidget.item(row_num, 2).text())
                
            elif action == item2:
                print("You chose the option 2, the context is", 
                      self.tableWidget.item(row_num, 0).text(), 
                      self.tableWidget.item(row_num, 1).text(), 
                      self.tableWidget.item(row_num, 2).text())
            
            elif action == item3:
                print("You chose the option 3, the context is", 
                      self.tableWidget.item(row_num, 0).text(), 
                      self.tableWidget.item(row_num, 1).text(), 
                      self.tableWidget.item(row_num, 2).text())
                
            else:
                
                return
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
        