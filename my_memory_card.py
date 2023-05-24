from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QPushButton)
from random import shuffle

class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question('Когда закончилась Вторая Мировая Война?', '1945', '1942', '1943', '1948')
q2 = Question('Самая дорогоя машина?', 'Rolce Royce Ghost', 'Ferrari Spider', 'McLaren', 'Matiz Best')
q3 = Question('Кто лучший футболист в мире?', 'Ronaldo', 'Messi', 'Mbappe', 'Hakimi')
q = Question('Сколько лет городу Бухара?', '2500', '1200', '3000', '2100')

question_list.append(q)
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)






app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400, 200)


question= QLabel('Сколько лет Ташкенту?')
r_btn_1 = QRadioButton('2700')
r_btn_2 = QRadioButton('10600')
r_btn_3 = QRadioButton('1000')
r_btn_4 = QRadioButton('5200')

btn = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов:')
h_line_group = QHBoxLayout()
v_line_group1 = QVBoxLayout()
v_line_group2 = QVBoxLayout()

v_line_group1.addWidget(r_btn_1)
v_line_group1.addWidget(r_btn_2)
v_line_group2.addWidget(r_btn_3)
v_line_group2.addWidget(r_btn_4)

h_line_group.addLayout(v_line_group1)
h_line_group.addLayout(v_line_group2)

RadioGroupBox.setLayout(h_line_group)

h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()
main_v_line = QVBoxLayout()

AnsGroupBox = QGroupBox('Правильный ответ')
result = QLabel('Прав ты или нет?')
correct = QLabel('Ответ будет здесь!')
ans_v_line = QVBoxLayout()
ans_v_line.addWidget(result, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
ans_v_line.addWidget(correct)
AnsGroupBox.setLayout(ans_v_line)

