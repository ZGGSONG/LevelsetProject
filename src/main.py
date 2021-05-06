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
        self.bn_image = ''

    @pyqtSlot()
    def on_img_tbtn_clicked(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, '选择一张图', '', 'images(*.png; *.jpg; *.jpeg; *.bmp);;*')
        if imgType[0]:
            self.bn_image = imgType[0]
        else:
            self.bn_image = './img/default.bmp'
        self.img_text.setText(f'{os.path.basename(self.bn_image)}')
        img = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.img_lab.setPixmap(img)
        return self.bn_image


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
