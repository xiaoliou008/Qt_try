import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QPushButton, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class FirstWindow(QMainWindow):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FirstWindow")
        self.resize(300, 300)
        self.status = self.statusBar()
        self.status.showMessage("欢迎使用", 5000)

        self.button1 = QPushButton("Exit")
        self.button1.clicked.connect(self.onClick_Button1)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
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

    def center(self):
        screen = QDesktopWidget().geometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2 - 100
        self.move(newLeft, newTop)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./questions.svg"))
    win = FirstWindow()
    sys.exit(app.exec_())
