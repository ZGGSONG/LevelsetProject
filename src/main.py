import os
import sys

from PyQt5.QtCore import pyqtSlot

from graduateproject import mwin
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon

from graduateproject.mwin import Ui_MainWindow


class MWim(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MWim, self).__init__(parent)
        self.setupUi(self)
        self.bn_image = ''

    @pyqtSlot()
    def on_img_tbtn_clicked(self):
        file = QFileDialog.getOpenFileName(self, '选择一张图', '', 'images(*.png; *.jpg; *.bmp);;*')
        if file[0]:
            self.bn_image = file[0]
        else:
            self.bn_image = 'default.bmp'
        self.img_text.setText(f'{os.path.basename(self.bn_image)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MWim()
    w.show()
    sys.exit(app.exec_())

# 旧版
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # 设置图标
#     app.setWindowIcon(QIcon('../graduateproject/logo.png'))
#
#     MainWindow = QMainWindow()
#
#     # 窗口
#     ui = mwin.Ui_MainWindow()
#     ui.actionOpen = ""
#     ui.setupUi(MainWindow)
#
#     # 显示窗口
#     MainWindow.show()
#     # 直至点击退出
#     sys.exit(app.exec_())
