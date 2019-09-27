import sys
import MiniDemo
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from expressiongeneration import Generationsystem

class MiniDemoWindow(QMainWindow):
    def __init__(self):
        super(MiniDemoWindow, self).__init__()
        ui = MiniDemo.Ui_MainWindow()

        self.generator = Generationsystem()
        self.genList = self.generator.generation2(2)
        self.gen_str = [str(i) for i in self.genList]
        self.expression = ''.join(self.gen_str)
        self.ans = eval(self.expression.replace("x", "*").replace("÷", "/"))
        self.initUI()

    def initUI(self):
        self.setWindowTitle('口算题生成器')
        self.label1 = QLabel()
        self.label1.setText(self.expression)
        self.label2 = QLabel()

        self.edit1 = QLineEdit()
        self.edit1.setValidator(QIntValidator())
        self.edit1.setPlaceholderText('计算结果')

        self.btn1 = QPushButton()
        self.btn1.setText('确定')
        self.btn1.clicked.connect(self.button_Pushed)

        layout = QFormLayout()
        layout.addRow('表达式：', self.label1)
        layout.addRow('请输入;', self.edit1)
        layout.addRow(self.btn1)
        layout.addRow('结果：', self.label2)
        self.widget0 = QWidget()
        self.widget0.setLayout(layout)
        self.setCentralWidget(self.widget0)
        self.show()


    def button_Pushed(self):
        ans_t = self.edit1.text()
        if(len(ans_t) > 0):
            if(eval(ans_t) == self.ans):
                self.label2.setText('正确')
                self.genList = self.generator.generation2(2)
                self.gen_str = [str(i) for i in self.genList]
                self.expression = ''.join(self.gen_str)
                self.ans = eval(self.expression.replace("x", "*").replace("÷", "/"))
                self.label1.setText(self.expression)
            else:
                self.label2.setText('错误')
        else:
            self.label2.setText('未输入结果')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MiniDemoWindow()
    sys.exit(app.exec())