import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class ComputeWindow(QMainWindow):
    def __init__(self):
        super(ComputeWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FirstWindow")
        self.resize(300, 300)

        self.status = self.statusBar()
        self.status.showMessage("欢迎使用", 5000)

        self.edit1 = QLineEdit()
        self.edit1.setValidator(QIntValidator())
        self.edit1.setPlaceholderText('请输入一个加数')
        self.edit1.textChanged.connect(self.input_Change)
        self.edit2 = QLineEdit()
        self.edit2.setValidator(QIntValidator())
        self.edit2.setPlaceholderText('请输入另一个加数')
        self.edit2.textChanged.connect(self.input_Change)
        self.edit3 = QLineEdit()
        self.edit3.isReadOnly()


        self.button1 = QPushButton("Exit")
        self.button1.clicked.connect(self.onClick_Button1)
        layout = QFormLayout()
        layout.addRow('plus1', self.edit1)
        layout.addRow('plus2', self.edit2)
        layout.addRow('result', self.edit3)
        layout.addRow('exit', self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
        self.center()
        self.show()

    def onClick_Button1(self):
        sender = self.sender()
        print(sender.text() + "Button is pushed")
        app = QApplication.instance()
        app.quit()

    def input_Change(self):
        first = self.edit1.text()
        second = self.edit2.text()
        if(len(first) > 0 and len(second) > 0):
            # print(int(first), int(second))
            self.edit3.setText(str(int(first) + int(second)))
            # print("change")

    def center(self):
        screen = QDesktopWidget().geometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2 - 100
        self.move(newLeft, newTop)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./questions.svg"))
    win = ComputeWindow()
    sys.exit(app.exec_())
