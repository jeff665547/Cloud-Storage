# PyQt5 進階介面控制項 (表格與樹 table and tree)
# QTableView的使用
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Table(QWidget):
    
    def __init__(self, arg = None):
        super(Table, self).__init__(arg)
        self.setWindowTitle("QTableView表格視圖控制項範例")
        self.resize(500, 300);
        self.model = QStandardItemModel(4, 4); # 儲存任意層級結構的資料
        self.model.setHorizontalHeaderLabels(["Label1", "Label2", "Label3", "Label4"])
        
        for row in range(4):
            for column in range(4):
                item = QStandardItem("row {}, column {}".format(row, column))
                self.model.setItem(row, column, item)
        
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        
        # (1) 讓表格填滿視窗(水平方向)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                
        
        # (2) 增加一整列新資料
        self.model.appendRow([
                    QStandardItem("row {}, column {}".format(11, 11)),
                    QStandardItem("row {}, column {}".format(11, 11)),
                    QStandardItem("row {}, column {}".format(11, 11)),
                    QStandardItem("row {}, column {}".format(11, 11))
                    ])
        
        # (3) 刪除目前選取的資料 (需另外寫function，在此僅列出做參考，不會work)
        # 取得目前選中的所有列
        indexs = self.tableView.selectionModel().selection().indexes()
        print(indexs)
        if len(indexs) > 0:
            # 取得第一列的索引
            index = indexs[0]
            self.model.removeRows(index.row(), 1)
        
        dlgLayout = QVBoxLayout();
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())
    