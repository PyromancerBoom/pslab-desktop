# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibration_loader.ui'


from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(832, 519)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.T1 = QtGui.QWidget()
        self.T1.setObjectName(_fromUtf8("T1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.T1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widgetFrameOuter = QtGui.QFrame(self.T1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet(_fromUtf8(""))
        self.widgetFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetFrameOuter.setObjectName(_fromUtf8("widgetFrameOuter"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.widgetFrameOuter)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.WidgetLayout = QtGui.QHBoxLayout()
        self.WidgetLayout.setObjectName(_fromUtf8("WidgetLayout"))
        self.verticalLayout.addLayout(self.WidgetLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame_2 = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 655, 450))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setMargin(2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.plot_area = QtGui.QGridLayout()
        self.plot_area.setObjectName(_fromUtf8("plot_area"))
        self.gridLayout_4.addLayout(self.plot_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.LegendFrame = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LegendFrame.sizePolicy().hasHeightForWidth())
        self.LegendFrame.setSizePolicy(sizePolicy)
        self.LegendFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.LegendFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LegendFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.LegendFrame.setObjectName(_fromUtf8("LegendFrame"))
        self.LegendLayout = QtGui.QVBoxLayout(self.LegendFrame)
        self.LegendLayout.setSpacing(2)
        self.LegendLayout.setMargin(2)
        self.LegendLayout.setObjectName(_fromUtf8("LegendLayout"))
        self.listWidget = QtGui.QListWidget(self.LegendFrame)
        self.listWidget.setMaximumSize(QtCore.QSize(120, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.LegendLayout.addWidget(self.listWidget)
        self.pushButton = QtGui.QPushButton(self.LegendFrame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.LegendLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.LegendFrame)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.widgetFrameOuter)
        self.tabWidget.addTab(self.T1, _fromUtf8(""))
        self.T2 = QtGui.QWidget()
        self.T2.setObjectName(_fromUtf8("T2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.T2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_7 = QtGui.QFrame(self.T2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QtCore.QSize(650, 16777215))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout = QtGui.QGridLayout(self.frame_7)
        self.gridLayout.setContentsMargins(0, 5, 0, 2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Frame_4 = QtGui.QFrame(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Frame_4.sizePolicy().hasHeightForWidth())
        self.Frame_4.setSizePolicy(sizePolicy)
        self.Frame_4.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame_4.setObjectName(_fromUtf8("Frame_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.Frame_4)
        self.gridLayout_5.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.line = QtGui.QFrame(self.Frame_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_5.addWidget(self.line, 0, 0, 1, 2)
        self.tableLayout = QtGui.QVBoxLayout()
        self.tableLayout.setObjectName(_fromUtf8("tableLayout"))
        self.gridLayout_5.addLayout(self.tableLayout, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.Frame_4, 0, 1, 1, 1)
        self.frame_4 = QtGui.QFrame(self.frame_7)
        self.frame_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.frame_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.ButtonSock = QtGui.QPushButton(self.frame_4)
        self.ButtonSock.setObjectName(_fromUtf8("ButtonSock"))
        self.verticalLayout_4.addWidget(self.ButtonSock)
        self.Button330 = QtGui.QPushButton(self.frame_4)
        self.Button330.setObjectName(_fromUtf8("Button330"))
        self.verticalLayout_4.addWidget(self.Button330)
        self.Button680 = QtGui.QPushButton(self.frame_4)
        self.Button680.setObjectName(_fromUtf8("Button680"))
        self.verticalLayout_4.addWidget(self.Button680)
        self.Button2220 = QtGui.QPushButton(self.frame_4)
        self.Button2220.setObjectName(_fromUtf8("Button2220"))
        self.verticalLayout_4.addWidget(self.Button2220)
        self.label_2 = QtGui.QLabel(self.frame_4)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.ButtonPCS = QtGui.QPushButton(self.frame_4)
        self.ButtonPCS.setObjectName(_fromUtf8("ButtonPCS"))
        self.verticalLayout_4.addWidget(self.ButtonPCS)
        self.resistance = QtGui.QDoubleSpinBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.resistance.setFont(font)
        self.resistance.setMinimum(50.0)
        self.resistance.setMaximum(10000.0)
        self.resistance.setProperty("value", 1000.0)
        self.resistance.setObjectName(_fromUtf8("resistance"))
        self.verticalLayout_4.addWidget(self.resistance)
        self.label_3 = QtGui.QLabel(self.frame_4)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.ButtonPCS_2 = QtGui.QPushButton(self.frame_4)
        self.ButtonPCS_2.setObjectName(_fromUtf8("ButtonPCS_2"))
        self.verticalLayout_4.addWidget(self.ButtonPCS_2)
        self.resistance_SEN = QtGui.QDoubleSpinBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.resistance_SEN.setFont(font)
        self.resistance_SEN.setMinimum(50.0)
        self.resistance_SEN.setMaximum(10000.0)
        self.resistance_SEN.setProperty("value", 1000.0)
        self.resistance_SEN.setObjectName(_fromUtf8("resistance_SEN"))
        self.verticalLayout_4.addWidget(self.resistance_SEN)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.ButtonReset = QtGui.QPushButton(self.frame_4)
        self.ButtonReset.setObjectName(_fromUtf8("ButtonReset"))
        self.verticalLayout_4.addWidget(self.ButtonReset)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        self.widgetLayout = QtGui.QHBoxLayout()
        self.widgetLayout.setObjectName(_fromUtf8("widgetLayout"))
        self.pushButton_9 = QtGui.QPushButton(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.widgetLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtGui.QPushButton(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.widgetLayout.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.widgetLayout, 1, 0, 1, 2)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.tabWidget.addTab(self.T2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.listWidget, QtCore.SIGNAL(_fromUtf8("currentTextChanged(QString)")), MainWindow.selected)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.crop)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.recover)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.upload)
        QtCore.QObject.connect(self.ButtonReset, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.reset)
        QtCore.QObject.connect(self.ButtonSock, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.calSock)
        QtCore.QObject.connect(self.Button330, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.cal330)
        QtCore.QObject.connect(self.Button680, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.cal680)
        QtCore.QObject.connect(self.Button2220, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.cal2220)
        QtCore.QObject.connect(self.ButtonPCS, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.calPCS)
        QtCore.QObject.connect(self.ButtonPCS_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.calSEN)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.LegendFrame.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.pushButton.setText(_translate("MainWindow", "Crop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.T1), _translate("MainWindow", "ADC, DAC and INL", None))
        self.frame_7.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.Frame_4.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.label.setText(_translate("MainWindow", "Click to Calibrate", None))
        self.ButtonSock.setText(_translate("MainWindow", "Socket Cap", None))
        self.Button330.setText(_translate("MainWindow", "330pF", None))
        self.Button680.setText(_translate("MainWindow", "680pF", None))
        self.Button2220.setText(_translate("MainWindow", "2220pF", None))
        self.ButtonPCS.setText(_translate("MainWindow", "PCS(0.5,1,1.5mA)", None))
        self.resistance.setSuffix(_translate("MainWindow", " Ohms", None))
        self.ButtonPCS_2.setText(_translate("MainWindow", "SEN", None))
        self.resistance_SEN.setSuffix(_translate("MainWindow", " Ohms", None))
        self.ButtonReset.setText(_translate("MainWindow", "Reset Calibration", None))
        self.pushButton_9.setText(_translate("MainWindow", "RECOVER", None))
        self.pushButton_8.setText(_translate("MainWindow", "UPLOAD", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.T2), _translate("MainWindow", "CAP, PCS, SEN", None))

