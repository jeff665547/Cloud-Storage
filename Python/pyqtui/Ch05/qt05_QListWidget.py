# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QListWidget的使用
# QListWidget是一個升級版本的QListView，它已經建立一個資料儲存模型(QListWidgetItem)。
# 只要呼叫addItem()函數，就能增加項目(Item)
# 在此例中，當按一下QListWidget列表中的某個項目時，將彈出訊息方塊，提示選擇的項目。
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You choose " + item.text())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    listWidget = ListWidget()
    listWidget.resize(300, 120)
    listWidget.addItem("Item 1")
    listWidget.addItem("Item 2")
    listWidget.addItem("Item 3")
    listWidget.addItem("Item 4")
    listWidget.setWindowTitle("QListwidget Example")
    listWidget.itemClicked.connect(listWidget.clicked)
    listWidget.show()
    sys.exit(app.exec_())