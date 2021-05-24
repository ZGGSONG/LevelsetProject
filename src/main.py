import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon

from levelsetproject.mwin import Ui_MainWindow


class MWim(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MWim, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../levelsetproject/logo.png'))
    w = MWim()
    w.show()
    sys.exit(app.exec_())
