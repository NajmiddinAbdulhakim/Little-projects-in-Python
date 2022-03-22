import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(400,400)

        self.main_windows = QWidget()
        self.main_layout = QVBoxLayout()
        self.input_filed_text = ""
        self.setFocus()
        # shu yerdan
        # leyout1
        self.layout1 = QVBoxLayout()
        self.input_filed = QLineEdit()
        self.input_filed.setMinimumHeight(40)
        self.input_filed.setFont(QFont("Times",15))
        self.input_filed.setAlignment(Qt.AlignRight)
        # self.input_filed.
        self.layout1.addWidget(self.input_filed)

        # layout2
        self.layout2 = QHBoxLayout()
        self.btn_c = QPushButton("C")
        self.btn_c.clicked.connect(self.input_cleaning)
        self.btn_percent = QPushButton("%")
        self.btn_plus_minus = QPushButton("+/-")
        self.btn_backspace = QPushButton("<--")
        self.btn_backspace.clicked.connect(self.remove_last_digit)
        self.add_contents(self.layout2.addWidget,self.btn_c,self.btn_percent,self.btn_plus_minus,self.btn_backspace)

        # layout3
        self.layout3 = QHBoxLayout()
        self.btn_7 = QPushButton("7")
        self.btn_7.clicked.connect(lambda: self.append_number("7"))
        self.btn_8 = QPushButton("8")
        self.btn_8.clicked.connect(lambda: self.append_number("8"))
        self.btn_9 = QPushButton("9")
        self.btn_9.clicked.connect(lambda: self.append_number("9"))
        self.btn_divide = QPushButton("/")
        self.add_contents(self.layout3.addWidget, self.btn_7, self.btn_8, self.btn_9, self.btn_divide)

        # layout4
        self.layout4 = QHBoxLayout()
        self.btn_4 = QPushButton("4")
        self.btn_4.clicked.connect(lambda: self.append_number("4"))
        self.btn_5 = QPushButton("5")
        self.btn_5.clicked.connect(lambda: self.append_number("5"))
        self.btn_6 = QPushButton("6")
        self.btn_6.clicked.connect(lambda: self.append_number("6"))
        self.btn_x = QPushButton("X")
        self.add_contents(self.layout4.addWidget, self.btn_4, self.btn_5, self.btn_6, self.btn_x)

        # layout5
        self.layout5 = QHBoxLayout()
        self.btn_1 = QPushButton("1")
        self.btn_1.clicked.connect(lambda: self.append_number("1"))
        self.btn_2 = QPushButton("2")
        self.btn_2.clicked.connect(lambda: self.append_number("2"))
        self.btn_3 = QPushButton("3")
        self.btn_3.clicked.connect(lambda: self.append_number("3"))
        self.btn_miuns = QPushButton("-")
        self.add_contents(self.layout5.addWidget, self.btn_1, self.btn_2, self.btn_3, self.btn_miuns)

        # layout6
        self.layout6 = QHBoxLayout()
        self.btn_0 = QPushButton("0")
        self.btn_0.clicked.connect(lambda: self.append_number("0"))
        self.btn_dot = QPushButton(".")
        self.btn_equal = QPushButton("=")
        self.btn_plas = QPushButton("+")
        self.add_contents(self.layout6.addWidget, self.btn_0, self.btn_dot, self.btn_equal, self.btn_plas)

        # Asosiy layout'ga qo'shish
        self.add_contents(self.main_layout.addLayout,self.layout1,self.layout2,
                          self.layout3,self.layout4,self.layout5,self.layout6,layout=True)

        # Shu yergacha

        self.main_windows.setLayout(self.main_layout)

        self.setCentralWidget(self.main_windows)
    @staticmethod
    def add_contents(metod_,*args,layout=False):
        if not layout:
            for btn in args:
                btn.setMinimumHeight(40)
                btn.setFont(QFont("Times",12))
                metod_(btn)
            return

        for i in args:
            metod_(i)

    def input_cleaning(self) -> None:
        self.input_filed_text = ""
        self.input_filed.setText("")

    def append_number(self,num: str) -> None:
        if self.input_filed_text == "0":
            self.update_input_filed(num)
            return
        self.update_input_filed(self.input_filed_text + num)

    def remove_last_digit(self) -> None:
        self.input_filed_text = self.input_filed_text[:-1]
        self.input_filed.setText(self.input_filed_text)

    def update_input_filed(self, str_: str) -> None:
        self.input_filed_text = str_
        self.input_filed.setText(self.input_filed_text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()