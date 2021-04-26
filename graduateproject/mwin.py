# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 951, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.img_lab = QtWidgets.QLabel(self.layoutWidget)
        self.img_lab.setText("")
        self.img_lab.setTextFormat(QtCore.Qt.AutoText)
        self.img_lab.setPixmap(QtGui.QPixmap(":/images/open.svg"))
        self.img_lab.setObjectName("img_lab")
        self.gridLayout_2.addWidget(self.img_lab, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.img_tbtn = QtWidgets.QToolButton(self.layoutWidget)
        self.img_tbtn.setMinimumSize(QtCore.QSize(30, 30))
        self.img_tbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img_tbtn.setObjectName("img_tbtn")
        self.gridLayout.addWidget(self.img_tbtn, 0, 2, 1, 1)
        self.img_text = QtWidgets.QLabel(self.layoutWidget)
        self.img_text.setMinimumSize(QtCore.QSize(30, 30))
        self.img_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img_text.setAlignment(QtCore.Qt.AlignCenter)
        self.img_text.setObjectName("img_text")
        self.gridLayout.addWidget(self.img_text, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.info = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.info.setFont(font)
        self.info.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.gridLayout_2.addWidget(self.info, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.ChanVese = QtWidgets.QWidget()
        self.ChanVese.setObjectName("ChanVese")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.ChanVese)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 70, 181, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("STKaiti")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setMidLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.line_4 = QtWidgets.QFrame(self.ChanVese)
        self.line_4.setGeometry(QtCore.QRect(60, 70, 20, 311))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.ChanVese)
        self.line_5.setGeometry(QtCore.QRect(240, 70, 20, 311))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.ChanVese)
        self.line_6.setGeometry(QtCore.QRect(70, 60, 181, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.ChanVese)
        self.line_7.setGeometry(QtCore.QRect(70, 370, 181, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.btn_cv = QtWidgets.QPushButton(self.ChanVese)
        self.btn_cv.setGeometry(QtCore.QRect(320, 70, 100, 32))
        self.btn_cv.setObjectName("btn_cv")
        self.tabWidget.addTab(self.ChanVese, "")
        self.RSF = QtWidgets.QWidget()
        self.RSF.setObjectName("RSF")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.RSF)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 70, 181, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("STKaiti")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setMidLineWidth(0)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setOpenExternalLinks(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setOpenExternalLinks(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setOpenExternalLinks(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.line_8 = QtWidgets.QFrame(self.RSF)
        self.line_8.setGeometry(QtCore.QRect(240, 70, 20, 311))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.RSF)
        self.line_9.setGeometry(QtCore.QRect(60, 70, 20, 311))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.RSF)
        self.line_10.setGeometry(QtCore.QRect(70, 370, 181, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.RSF)
        self.line_11.setGeometry(QtCore.QRect(70, 60, 181, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.tabWidget.addTab(self.RSF, "")
        self.DRLSE = QtWidgets.QWidget()
        self.DRLSE.setObjectName("DRLSE")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.DRLSE)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 70, 181, 311))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("STKaiti")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_15.setMidLineWidth(0)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setOpenExternalLinks(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setOpenExternalLinks(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setOpenExternalLinks(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setOpenExternalLinks(True)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setOpenExternalLinks(True)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setOpenExternalLinks(True)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.line_12 = QtWidgets.QFrame(self.DRLSE)
        self.line_12.setGeometry(QtCore.QRect(240, 70, 20, 311))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.DRLSE)
        self.line_13.setGeometry(QtCore.QRect(60, 70, 20, 311))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.DRLSE)
        self.line_14.setGeometry(QtCore.QRect(70, 370, 181, 20))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.DRLSE)
        self.line_15.setGeometry(QtCore.QRect(70, 60, 181, 20))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.tabWidget.addTab(self.DRLSE, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1021, 24))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menuhelp = QtWidgets.QMenu(self.menuBar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionhelp.setIcon(icon2)
        self.actionhelp.setObjectName("actionhelp")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName("actionClose")
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSave_As)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menuhelp.addAction(self.actionhelp)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionClose.triggered.connect(MainWindow.close)
        self.btn_cv.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "水平集分割效果测试"))
        self.img_tbtn.setText(_translate("MainWindow", "..."))
        self.img_text.setText(_translate("MainWindow", "请选择图像..."))
        self.info.setText(_translate("MainWindow", "水平集模型选择"))
        self.label_2.setText(_translate("MainWindow", "相关资料"))
        self.label.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_3.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_4.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_5.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_6.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_7.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.btn_cv.setText(_translate("MainWindow", "点击运行CV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ChanVese), _translate("MainWindow", "CV模型"))
        self.label_8.setText(_translate("MainWindow", "相关资料"))
        self.label_9.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_10.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_11.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_12.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_13.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_14.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RSF), _translate("MainWindow", "LBF模型"))
        self.label_15.setText(_translate("MainWindow", "相关资料"))
        self.label_16.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_17.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_18.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_19.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_20.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.label_21.setText(_translate("MainWindow", "<a href=\'https://math.berkeley.edu/~sethian/2006/Publications/Menu_Expanded_Publications.html\'>Level Set 必读刊物</a>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DRLSE), _translate("MainWindow", "正则模型"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menuhelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionhelp.setText(_translate("MainWindow", "Help"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
from graduateproject import res_rc
