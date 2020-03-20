#!/usr/bin/env python3

import csv
import random
import sys
from PyQt5 import QtWidgets

from window import Ui_MainWindow as ExamWindow


file = open('abbr.csv')
reader = csv.reader(file)
data_table = [row for row in reader]
file.close()
print('Read', len(data_table), 'abbreviations.')


app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
ui = ExamWindow()
ui.setupUi(main_window)
ui.menubar.hide()

data_row_picked = None
count = 0


def pick_abbr():
    if count > 0:
        ui.lineEdit.returnPressed.disconnect()
    index = random.randint(0, len(data_table) - 1)
    global data_row_picked
    data_row_picked = data_table[index]
    ui.abbr.setText(data_row_picked[0])
    ui.lineEdit.clear()
    ui.lineEdit.returnPressed.connect(submit)
    ui.msg.setText('<p>Please input the full name.</p><p>Press enter to submit answer.</p>')


def submit():
    global count
    count += 1
    ui.lineEdit.returnPressed.disconnect()
    if ui.lineEdit.text().strip().lower() == data_row_picked[1].lower():
        ui.msg.setText('<p style="color: green">Correct!</p><p>Press enter to go next.')
    else:
        msg = """
        <p><span style="color: red">Wrong!</span> Correct answer is:</p>
        <p style="color: orange">%s</p>
        <p>Press enter to go next.</p>
        """ % data_row_picked[1]
        ui.msg.setText(msg)
    ui.lineEdit.returnPressed.connect(pick_abbr)


pick_abbr()

main_window.show()
sys.exit(app.exec_())
