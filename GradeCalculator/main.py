from PyQt5.QtWidgets import *
import sys
from GradeCalculator import ui

SUBJECT_LIST = [
    "Software and Network Engineering",
    "Software Systems Engineering",
    "Failure Analysis",
    "Tools of Operations Research",
    "Systems Engineering",
    "Foundation of Tech Ethics & Values",
]


class MainApp(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(591, 297)
        self.setWindowTitle("Grade Calculator")
        for subject in SUBJECT_LIST:
            self.subjects_dropdown.addItem(str(subject))

        self.weight_input.setPlaceholderText('Enter Weight / Percentage ')
        self.result_btn.clicked.connect(self.generateResults)

    def showWarningBox(self, title='Error', text=''):
        QMessageBox.about(self, title, str(text))

    def generateResults(self):
        self.result_label.setText("")
        self.result_label.setStyleSheet(f"background-color:none")

        weight = self.weight_input.text()
        subject = self.subjects_dropdown.currentText()
        if subject not in SUBJECT_LIST:
            return self.showWarningBox(text="Please select a Subject !")

        try:
            weight = float(str(weight))
        except:
            return self.showWarningBox(text="Weight / Percentage must be numeric !")
        if weight < 0 or weight > 100:
            return self.showWarningBox(text="Weight / Percentage must be in Range 0-100")

        if weight <= 59.4:
            bg_color = "#ff2d19"
            grade = 'F'
        elif weight >= 59.5 and weight <= 69.4:
            bg_color = "#ff9d4d"
            grade = 'D'
        elif weight >= 69.5 and weight <= 79.4:
            bg_color = "#fff64d"
            grade = 'C'
        elif weight >= 79.5 and weight <= 89.4:
            bg_color = "#4e2ffa"
            grade = 'B'
        elif weight >= 89.5 and weight <= 100:
            bg_color = "#32fa4d"
            grade = 'A'

        self.result_label.setStyleSheet(f"background-color:{bg_color}")
        self.result_label.setText(F"Your Grade is {grade}")


def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()