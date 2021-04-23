import sys

from graduateproject import mwin
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../graduateproject/logo.png'))
    MainWindow = QMainWindow()

    # 窗口
    ui = mwin.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
