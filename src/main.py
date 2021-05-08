import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui

from levelsetproject.mwin import Ui_MainWindow


class MWim(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MWim, self).__init__()
        self.setupUi(self)
        # self.img_path = ''

    # @pyqtSlot()
    # def on_img_tbtn_clicked(self):
    #     imgType = QFileDialog.getOpenFileName(self, '选择一张图', '', 'images(*.png; *.jpg; *.jpeg; *.bmp);;*')
    #     if imgType[0]:
    #         self.img_path = imgType[0]
    #     else:
    #         self.img_path = './img/default.bmp'
    #     self.img_text.setText(f'{os.path.basename(self.img_path)}')
    #     img = QtGui.QPixmap(imgType).scaled(self.img_lab.width(), self.img_lab.height())
    #     self.img_lab.setPixmap(img)
    #     return self.img_path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../levelsetproject/logo.png'))
    w = MWim()
    w.show()
    sys.exit(app.exec_())

# 旧版
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # 设置图标
#     app.setWindowIcon(QIcon('../levelsetproject/logo.png'))
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
