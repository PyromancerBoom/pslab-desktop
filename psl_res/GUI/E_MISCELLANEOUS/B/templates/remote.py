# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote.ui'


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
        MainWindow.resize(858, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout = QtGui.QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setContentsMargins(-1, 2, 2, 2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.channelLabel = QtGui.QLabel(self.frame_2)
        self.channelLabel.setObjectName(_fromUtf8("channelLabel"))
        self.gridLayout.addWidget(self.channelLabel, 2, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.frame_2)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.pubEdit = QtGui.QLineEdit(self.frame_2)
        self.pubEdit.setText(_fromUtf8(""))
        self.pubEdit.setObjectName(_fromUtf8("pubEdit"))
        self.gridLayout.addWidget(self.pubEdit, 1, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.subEdit = QtGui.QLineEdit(self.frame_2)
        self.subEdit.setText(_fromUtf8(""))
        self.subEdit.setObjectName(_fromUtf8("subEdit"))
        self.gridLayout.addWidget(self.subEdit, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.cmdEdit = QtGui.QLineEdit(self.frame_4)
        self.cmdEdit.setObjectName(_fromUtf8("cmdEdit"))
        self.gridLayout_3.addWidget(self.cmdEdit, 0, 0, 1, 1)
        self.sendID = QtGui.QLineEdit(self.frame_4)
        self.sendID.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sendID.setObjectName(_fromUtf8("sendID"))
        self.gridLayout_3.addWidget(self.sendID, 0, 2, 1, 1)
        self.responseLabel = QtGui.QLabel(self.frame_4)
        self.responseLabel.setObjectName(_fromUtf8("responseLabel"))
        self.gridLayout_3.addWidget(self.responseLabel, 1, 0, 1, 3)
        self.pushButton_3 = QtGui.QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.results = QtGui.QTextEdit(self.frame_3)
        self.results.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.results.setObjectName(_fromUtf8("results"))
        self.gridLayout_2.addWidget(self.results, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame_5 = QtGui.QFrame(self.tab_2)
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setContentsMargins(-1, 2, 2, 2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.thingSpeakKey = QtGui.QLineEdit(self.frame_5)
        self.thingSpeakKey.setObjectName(_fromUtf8("thingSpeakKey"))
        self.gridLayout_4.addWidget(self.thingSpeakKey, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.results_2 = QtGui.QTextBrowser(self.tab_2)
        self.results_2.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.results_2.setObjectName(_fromUtf8("results_2"))
        self.verticalLayout_4.addWidget(self.results_2)
        self.frame_6 = QtGui.QFrame(self.tab_2)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.thingSpeakInterval = QtGui.QSpinBox(self.frame_6)
        self.thingSpeakInterval.setMinimum(15)
        self.thingSpeakInterval.setMaximum(1000)
        self.thingSpeakInterval.setObjectName(_fromUtf8("thingSpeakInterval"))
        self.gridLayout_5.addWidget(self.thingSpeakInterval, 0, 4, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_5.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.cmdEditThingSpeak = QtGui.QLineEdit(self.frame_6)
        self.cmdEditThingSpeak.setObjectName(_fromUtf8("cmdEditThingSpeak"))
        self.gridLayout_5.addWidget(self.cmdEditThingSpeak, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame_6)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.setListenState)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.resetKeys)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.execRemote)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.setThingSpeakCommand)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote access and publishing", None))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.channelLabel.setText(_translate("MainWindow", "channel:", None))
        self.checkBox.setText(_translate("MainWindow", "Listen to incoming messages", None))
        self.pubEdit.setPlaceholderText(_translate("MainWindow", "publish key", None))
        self.pushButton_4.setText(_translate("MainWindow", "Reset keys", None))
        self.subEdit.setPlaceholderText(_translate("MainWindow", "subscriber key", None))
        self.frame_3.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.frame_4.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.cmdEdit.setText(_translate("MainWindow", "get_version()", None))
        self.sendID.setText(_translate("MainWindow", "0x02", None))
        self.responseLabel.setText(_translate("MainWindow", "Response:", None))
        self.pushButton_3.setText(_translate("MainWindow", "Execute on", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "PubNub", None))
        self.frame_5.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.thingSpeakKey.setToolTip(_translate("MainWindow", "Get a key from thingspeak.com by creating your own channel", None))
        self.thingSpeakKey.setText(_translate("MainWindow", "H1OE0R294J0R6YQN", None))
        self.thingSpeakKey.setPlaceholderText(_translate("MainWindow", "publish key", None))
        self.label_2.setText(_translate("MainWindow", "ThingSpeak Key", None))
        self.frame_6.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.thingSpeakInterval.setToolTip(_translate("MainWindow", "Set the interval for pushing data.\n"
"The rate limit for ThingSpeak.com is 15 seconds", None))
        self.thingSpeakInterval.setSuffix(_translate("MainWindow", " Seconds", None))
        self.pushButton_6.setText(_translate("MainWindow", "Set Command", None))
        self.cmdEditThingSpeak.setText(_translate("MainWindow", "get_average_voltage(\'CH1\')", None))
        self.cmdEditThingSpeak.setPlaceholderText(_translate("MainWindow", "Command to execute", None))
        self.label.setText(_translate("MainWindow", "Update Interval", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ThingSpeak", None))

