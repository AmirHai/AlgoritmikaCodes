import sys
from random import shuffle

from PyQt5.QtGui import QFont
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MemoryCard(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('Memory Card')

        self.initUI()


    def initUI(self):
        self.mainVLayout = QVBoxLayout()
        self.setLayout(self.mainVLayout)

        self.question_text = QLabel('Самый сложный вопрос!')
        self.mainVLayout.addWidget(self.question_text, alignment=Qt.AlignmentFlag.AlignCenter, stretch=1)

        self.buttonGroup = QButtonGroup()
        self.answers = []
        self.variantsBox = QGroupBox()
        self.gridlayout = QGridLayout()

        for i in range(4):
            btn = QRadioButton()
            btn.setText(f'ответ {i+1}')
            self.gridlayout.addWidget(btn, i // 2, i % 2)
            self.buttonGroup.addButton(btn)
            self.answers.append(btn)
        self.variantsBox.setLayout(self.gridlayout)
        self.mainVLayout.addWidget(self.variantsBox, 4)

        self.ansGroupBox = QGroupBox()
        self.Vlayout = QVBoxLayout()
        self.ansGroupBox.setLayout(self.Vlayout)
        self.mainVLayout.addWidget(self.ansGroupBox, 4)

        self.TrueFalselbl = QLabel('Правильно/неправильно')
        self.answerlbl = QLabel('Правильный ответ')
        self.Vlayout.addWidget(self.TrueFalselbl, alignment=Qt.AlignmentFlag.AlignLeft)
        self.Vlayout.addWidget(self.answerlbl, alignment=Qt.AlignmentFlag.AlignCenter)

        self.answerButton = QPushButton('Ответить')
        self.answerButton.clicked.connect(self.start_test)
        self.mainVLayout.addWidget(self.answerButton, 1)

        self.ask('самая большая планета?', 'Юпитер', 'Земля', 'Плутон', 'Сатурн')
        self.ansGroupBox.hide()

    def show_correct(self):
        self.ansGroupBox.show()
        self.variantsBox.hide()
        self.answerButton.setText('Следующий вопрос')

    def show_question(self):
        self.ansGroupBox.hide()
        self.variantsBox.show()
        self.answerButton.setText('Ответить')
        self.buttonGroup.setExclusive(False)
        for btn in self.answers:
            btn.setChecked(False)
        self.buttonGroup.setExclusive(True)

    def start_test(self):
        if self.answerButton.text() == 'Ответить':
            self.check_answer()
            self.show_correct()
        else:
            self.show_question()
            self.ask('самая большая планета?','Юпитер', 'Земля', 'Плутон', 'Сатурн')

    def ask(self, question, right, wrong1, wrong2, wrong3):
        self.question_text.setText(question)
        shuffle(self.answers)
        self.answers[0].setText(right)
        self.answers[1].setText(wrong1)
        self.answers[2].setText(wrong2)
        self.answers[3].setText(wrong3)

    def check_answer(self):
        if self.answers[0].isChecked():
            self.TrueFalselbl.setText('Правильно!')
        if self.answers[1].isChecked():
            self.TrueFalselbl.setText('Неправильно!')
        if self.answers[2].isChecked():
            self.TrueFalselbl.setText('Неправильно!')
        if self.answers[3].isChecked():
            self.TrueFalselbl.setText('Неправильно!')
        self.answerlbl.setText(f'Правильный ответ: {self.answers[0].text()}')




if '__main__' == __name__:
    app = QApplication(sys.argv)
    window = MemoryCard()
    window.show()
    sys.exit(app.exec())
