from PyQt5 import QtWidgets, QtCore, QtGui

import sys

class CtmWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)

        self.button = QtWidgets.QPushButton("Close Overlay")
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().addWidget(self.button)

        self.button.clicked.connect(self.hideOverlay)

    def paintEvent(self, event):

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), 10, 10)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        pen = QtGui.QPen(QtCore.Qt.white, 1)
        painter.setPen(pen)
        painter.fillPath(path, QtCore.Qt.white)
        painter.drawPath(path)
        painter.end()

    def hideOverlay(self):
        self.parent().hide()



class Overlay(QtWidgets.QWidget):
    def __init__(self, parent, widget):
        QtWidgets.QWidget.__init__(self, parent)
        palette = QtGui.QPalette(self.palette())
        palette.setColor(palette.Background, QtCore.Qt.transparent)
        self.setPalette(palette)

        self.widget = widget
        self.widget.setParent(self)


    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillRect(event.rect(), QtGui.QBrush(QtGui.QColor(0, 0, 0, 127)))
        painter.end()

    def resizeEvent(self, event):
        position_x = (self.frameGeometry().width()-self.widget.frameGeometry().width())/2
        position_y = (self.frameGeometry().height()-self.widget.frameGeometry().height())/2

        self.widget.move(position_x, position_y)
        event.accept()

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(800, 500)

        self.button = QtWidgets.QPushButton("Click Me")

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.button)
        self.popup = Overlay(self, CtmWidget())
        self.popup.hide()

        # Connections
        self.button.clicked.connect(self.displayOverlay)

    def displayOverlay(self):
        self.popup.show()
        print("clicked")

    def resizeEvent(self, event):
        self.popup.resize(event.size())
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())