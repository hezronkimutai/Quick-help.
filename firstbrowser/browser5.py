from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout)

import sys

class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()

        b1=QPushButton("Button1")
        b2=QPushButton("Button2")
        b3=QPushButton("Button3")
        b4=QPushButton("Button4")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)
        mainLayout.addWidget(b3)
        mainLayout.addWidget(b4)

        self.setLayout(mainLayout)
        self.setWindowTitle("Form Layout - pythonspot.com")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
