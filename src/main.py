import sys

from graduateproject import mwin
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('../graduateproject/logo.png'))

    MainWindow = QMainWindow()

    # 窗口
    ui = mwin.Ui_MainWindow()
    ui.actionOpen = ""
    ui.setupUi(MainWindow)

    # 显示窗口
    MainWindow.show()
    # 直至点击退出
    sys.exit(app.exec_())
