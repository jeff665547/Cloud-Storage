import sys
import time
import numpy as np
from functools import partial

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QTimer
from PyQt5.QtWidgets import (QDialog, QApplication, QPushButton, 
                             QGridLayout, QProgressBar, QLabel)

# 直接將中斷的程序分成兩部分來執行，在兩部分中間安插dialog的對話視窗
class SpecialDialog(QDialog):
    def __init__(self):
        super().__init__()
        btn = QPushButton("pass variable")
        btn.clicked.connect(self.accept)
        layout = QGridLayout()
        layout.addWidget(btn)
        self.setLayout(layout)
        self.variable = np.random.randint(0, 100)

# Object, which will be moved to another thread B. (Different from GUI thread (MainWindow, and SpecialDialog).)
class Handler(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._isRunning = True
        self._success = False
    
    # Methods, which will execute algorithm in another thread B.
    @pyqtSlot()
    def task_1(self):
        i = 0
        while i <= 50 and self._isRunning:
            time.sleep(0.01)
            i += 1
            # send signal with an integral (i) from the thread B.
            self.progress.emit(i)

    @pyqtSlot(int)
    def task_2(self, result):
        i = 51
        while i < 100 and self._isRunning:
            time.sleep(0.01)
            i += 1
            # send signal with an integral (i) from the thread B.
            self.progress.emit(i)

        if i == 100:
            self._success = True
            # send signal with an integral (result) from the thread B.
            self.finished.emit(result)

    def stop(self):
        self._isRunning = False
        


class MainWindow(QDialog):
    contin = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        btn = QPushButton("test")
        
        # Use button to invoke slot.
        btn.clicked.connect(self.run_test)
        
        self.pbar = QProgressBar()
        self.resultLabel = QLabel("Result:")
        layout = QGridLayout(self)
        layout.addWidget(btn)
        layout.addWidget(self.pbar)
        layout.addWidget(self.resultLabel)
        self.setLayout(layout)

        
        # Create thread B.
        self.handler_thread = QThread()
        self.handler = None
        self.result = None

    def run_test(self):
        
        # Create the object (without a parent, so that it can be moved to another thread.) 
        # which will be moved to the thread B.
        self.handler = Handler()
        # Move the object to the thread B.
        self.handler.moveToThread(self.handler_thread)
        
        # After that, we can connect signals from this object to slots (progress, finisher) in GUI thread.
        self.handler.progress.connect(self.progress)
        self.handler.finished.connect(self.finisher)
        
        # Connect started signal to the task_1 method of object in the thread B.
        self.handler_thread.started.connect(self.handler.task_1)
        
        # Start thread (All methods of self.handler are now executed in the thread B.)
        self.handler_thread.start()

    @pyqtSlot(int)
    def progress(self, val):
        self.pbar.setValue(val)
        
        if val == 50:
            self.dialog = SpecialDialog()
            self.dialog.exec_()
            result = self.dialog.variable
            wrapper = partial(self.handler.task_2, result)
            QTimer.singleShot(0, wrapper)
            
    @pyqtSlot(int)
    def finisher(self, result):
        self.result = result
        self.resultLabel.setText(f"Result: {result}")
        self.pbar.setValue(0)
        # self.handler.stop()
        self.handler_thread.quit()
        self.handler_thread.wait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())    
