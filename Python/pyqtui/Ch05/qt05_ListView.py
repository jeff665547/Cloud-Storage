# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QListView的使用
# QListView用來展示資料(呈現方式為清單模式)，其子類是QListWidget。
# QListView是基於模型(Model)的類別，要求程式先建立模型，再保存資料。
# 在此例中，當按一下QListView控制項Model中的某項目時，將彈出訊息方塊(提示選擇的項目)
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QListView, QMessageBox)
from PyQt5.QtCore import QStringListModel
import sys

class ListViewDemo(QWidget):
    def __init__(self, parent = None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView Example")
        self.resize(300, 270)
        layout = QVBoxLayout()
        
        listView = QListView()
        slm = QStringListModel();
        self.qList = ["Item 1", "Item 2", "Item 3", "Item 4"]
        slm.setStringList(self.qList)
        listView.setModel(slm)
        listView.clicked.connect(self.clicked)
        layout.addWidget(listView)
        self.setLayout(layout)
        
    def clicked(self, qModelIndex):
        QMessageBox.information(self, "ListWidget", "You choose " + 
                                self.qList[qModelIndex.row()])
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())