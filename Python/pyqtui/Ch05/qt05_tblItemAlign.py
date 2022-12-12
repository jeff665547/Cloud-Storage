# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableWidget的使用
# 2. 設定儲存格
# 設定儲存格文字的對齊方式
# 在Qt的官方說明文件中，
# QTableWidgetItem.setTextAlignment(int)用來設定儲存格中文字的對齊方式
# 該函數的參數為對齊方式的列舉值。
# 在此例中，將表格中的其中一格裡的文字靠右對其並與底部對齊
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

        newItem = QTableWidgetItem("John")
        tableWidget.setItem(0, 0, newItem)  
        newItem.setTextAlignment( Qt.AlignRight | Qt.AlignBottom ) 
        # 靠右對齊並與底部對齊

        newItem = QTableWidgetItem("boy")
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("170")
        tableWidget.setItem(0, 2, newItem)     

        newItem = QTableWidgetItem("Jeff")
        tableWidget.setItem(1, 0, newItem)  

        newItem = QTableWidgetItem("boy")
        tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem("183")
        tableWidget.setItem(1, 2, newItem)     

        newItem = QTableWidgetItem("Alice")
        tableWidget.setItem(2, 0, newItem)  

        newItem = QTableWidgetItem("girl")
        tableWidget.setItem(2, 1, newItem)

        newItem = QTableWidgetItem("163")
        tableWidget.setItem(2, 2, newItem)     

        newItem = QTableWidgetItem("Tina")
        tableWidget.setItem(3, 0, newItem)  

        newItem = QTableWidgetItem("girl")
        tableWidget.setItem(3, 1, newItem)

        newItem = QTableWidgetItem("175")
        tableWidget.setItem(3, 2, newItem)     

        tableWidget.sortItems(2, Qt.DescendingOrder) #沿著第二個column做降冪排列
        
        self.setLayout(conLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())