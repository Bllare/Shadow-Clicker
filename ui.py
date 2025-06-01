# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainBFzoGl.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(528, 543)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_clickerType_clickerInterval = QHBoxLayout()
        self.layout_clickerType_clickerInterval.setObjectName(u"layout_clickerType_clickerInterval")
        self.groupBox_clickType = QGroupBox(self.centralwidget)
        self.groupBox_clickType.setObjectName(u"groupBox_clickType")
        self.groupBox_clickType.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_clickType)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 20, 0)
        self.radioButton_normalClicker = QRadioButton(self.groupBox_clickType)
        self.radioButton_normalClicker.setObjectName(u"radioButton_normalClicker")
        self.radioButton_normalClicker.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton_normalClicker)

        self.layout_insideClicker = QHBoxLayout()
        self.layout_insideClicker.setObjectName(u"layout_insideClicker")
        self.radioButton_insideClicker = QRadioButton(self.groupBox_clickType)
        self.radioButton_insideClicker.setObjectName(u"radioButton_insideClicker")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_insideClicker.sizePolicy().hasHeightForWidth())
        self.radioButton_insideClicker.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.radioButton_insideClicker.setFont(font)
        self.radioButton_insideClicker.setLayoutDirection(Qt.LeftToRight)

        self.layout_insideClicker.addWidget(self.radioButton_insideClicker)

        self.Spacer_insideClicker = QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_insideClicker.addItem(self.Spacer_insideClicker)

        self.label_hwnd = QLabel(self.groupBox_clickType)
        self.label_hwnd.setObjectName(u"label_hwnd")

        self.layout_insideClicker.addWidget(self.label_hwnd)

        self.spinBox_hwnd = QSpinBox(self.groupBox_clickType)
        self.spinBox_hwnd.setObjectName(u"spinBox_hwnd")
        self.spinBox_hwnd.setMinimumSize(QSize(80, 0))
        font1 = QFont()
        font1.setKerning(True)
        self.spinBox_hwnd.setFont(font1)
        self.spinBox_hwnd.setMaximum(999999999)

        self.layout_insideClicker.addWidget(self.spinBox_hwnd)


        self.verticalLayout_4.addLayout(self.layout_insideClicker)


        self.layout_clickerType_clickerInterval.addWidget(self.groupBox_clickType)

        self.groupBox_clickerInterval = QGroupBox(self.centralwidget)
        self.groupBox_clickerInterval.setObjectName(u"groupBox_clickerInterval")
        self.groupBox_clickerInterval.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_clickerInterval)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.spinBox_mins = QSpinBox(self.groupBox_clickerInterval)
        self.spinBox_mins.setObjectName(u"spinBox_mins")
        self.spinBox_mins.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_mins.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.spinBox_mins)

        self.label_mins = QLabel(self.groupBox_clickerInterval)
        self.label_mins.setObjectName(u"label_mins")

        self.horizontalLayout_5.addWidget(self.label_mins)

        self.spinBox_secs = QSpinBox(self.groupBox_clickerInterval)
        self.spinBox_secs.setObjectName(u"spinBox_secs")
        self.spinBox_secs.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_secs.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.spinBox_secs)

        self.label_secs = QLabel(self.groupBox_clickerInterval)
        self.label_secs.setObjectName(u"label_secs")

        self.horizontalLayout_5.addWidget(self.label_secs)

        self.spinBox_miliseconds = QSpinBox(self.groupBox_clickerInterval)
        self.spinBox_miliseconds.setObjectName(u"spinBox_miliseconds")
        self.spinBox_miliseconds.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_miliseconds.setMinimum(0)
        self.spinBox_miliseconds.setMaximum(9999)
        self.spinBox_miliseconds.setValue(100)

        self.horizontalLayout_5.addWidget(self.spinBox_miliseconds)

        self.label_miliseconds = QLabel(self.groupBox_clickerInterval)
        self.label_miliseconds.setObjectName(u"label_miliseconds")

        self.horizontalLayout_5.addWidget(self.label_miliseconds)


        self.layout_clickerType_clickerInterval.addWidget(self.groupBox_clickerInterval)


        self.verticalLayout_2.addLayout(self.layout_clickerType_clickerInterval)

        self.layout_clickerOptionsAndRepeat = QHBoxLayout()
        self.layout_clickerOptionsAndRepeat.setObjectName(u"layout_clickerOptionsAndRepeat")
        self.groupBox_clickerOptions = QGroupBox(self.centralwidget)
        self.groupBox_clickerOptions.setObjectName(u"groupBox_clickerOptions")
        self.groupBox_clickerOptions.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.groupBox_clickerOptions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.layout_clickButton = QHBoxLayout()
        self.layout_clickButton.setObjectName(u"layout_clickButton")
        self.label_clickButton = QLabel(self.groupBox_clickerOptions)
        self.label_clickButton.setObjectName(u"label_clickButton")

        self.layout_clickButton.addWidget(self.label_clickButton)

        self.comboBox_clickButton = QComboBox(self.groupBox_clickerOptions)
        self.comboBox_clickButton.addItem("")
        self.comboBox_clickButton.addItem("")
        self.comboBox_clickButton.addItem("")
        self.comboBox_clickButton.setObjectName(u"comboBox_clickButton")

        self.layout_clickButton.addWidget(self.comboBox_clickButton)


        self.verticalLayout.addLayout(self.layout_clickButton)

        self.layout_clickType = QHBoxLayout()
        self.layout_clickType.setObjectName(u"layout_clickType")
        self.label_clickType = QLabel(self.groupBox_clickerOptions)
        self.label_clickType.setObjectName(u"label_clickType")

        self.layout_clickType.addWidget(self.label_clickType)

        self.comboBox_clickType = QComboBox(self.groupBox_clickerOptions)
        self.comboBox_clickType.addItem("")
        self.comboBox_clickType.addItem("")
        self.comboBox_clickType.setObjectName(u"comboBox_clickType")

        self.layout_clickType.addWidget(self.comboBox_clickType)


        self.verticalLayout.addLayout(self.layout_clickType)


        self.layout_clickerOptionsAndRepeat.addWidget(self.groupBox_clickerOptions)

        self.groupBox_repeat = QGroupBox(self.centralwidget)
        self.groupBox_repeat.setObjectName(u"groupBox_repeat")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_repeat)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 8)
        self.layout_repeat = QHBoxLayout()
        self.layout_repeat.setObjectName(u"layout_repeat")
        self.radioButton_repeat = QRadioButton(self.groupBox_repeat)
        self.radioButton_repeat.setObjectName(u"radioButton_repeat")

        self.layout_repeat.addWidget(self.radioButton_repeat)

        self.spinBox_repeat = QSpinBox(self.groupBox_repeat)
        self.spinBox_repeat.setObjectName(u"spinBox_repeat")
        self.spinBox_repeat.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_repeat.setMinimum(1)
        self.spinBox_repeat.setMaximum(999999999)
        self.spinBox_repeat.setValue(1)

        self.layout_repeat.addWidget(self.spinBox_repeat)

        self.label_repeat = QLabel(self.groupBox_repeat)
        self.label_repeat.setObjectName(u"label_repeat")

        self.layout_repeat.addWidget(self.label_repeat)


        self.verticalLayout_3.addLayout(self.layout_repeat)

        self.radioButton_repeatUntilStopped = QRadioButton(self.groupBox_repeat)
        self.radioButton_repeatUntilStopped.setObjectName(u"radioButton_repeatUntilStopped")
        self.radioButton_repeatUntilStopped.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_repeatUntilStopped)


        self.layout_clickerOptionsAndRepeat.addWidget(self.groupBox_repeat)


        self.verticalLayout_2.addLayout(self.layout_clickerOptionsAndRepeat)

        self.groupBox_cursorPosition = QGroupBox(self.centralwidget)
        self.groupBox_cursorPosition.setObjectName(u"groupBox_cursorPosition")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_cursorPosition)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.radioButton_currentLocation = QRadioButton(self.groupBox_cursorPosition)
        self.radioButton_currentLocation.setObjectName(u"radioButton_currentLocation")
        self.radioButton_currentLocation.setMaximumSize(QSize(110, 16777215))
        self.radioButton_currentLocation.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_currentLocation)

        self.spacer_cursorPosition = QSpacerItem(60, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.spacer_cursorPosition)

        self.radioButton_customLocation = QRadioButton(self.groupBox_cursorPosition)
        self.radioButton_customLocation.setObjectName(u"radioButton_customLocation")
        self.radioButton_customLocation.setMaximumSize(QSize(20, 20))
        self.radioButton_customLocation.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.radioButton_customLocation)

        self.pushButton_pickLocation = QPushButton(self.groupBox_cursorPosition)
        self.pushButton_pickLocation.setObjectName(u"pushButton_pickLocation")
        self.pushButton_pickLocation.setMinimumSize(QSize(85, 35))
        self.pushButton_pickLocation.setMaximumSize(QSize(25, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        self.pushButton_pickLocation.setFont(font2)

        self.horizontalLayout_4.addWidget(self.pushButton_pickLocation)

        self.lable_x = QLabel(self.groupBox_cursorPosition)
        self.lable_x.setObjectName(u"lable_x")
        self.lable_x.setMaximumSize(QSize(15, 16777215))
        self.lable_x.setFont(font)
        self.lable_x.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lable_x)

        self.spinBox_x = QSpinBox(self.groupBox_cursorPosition)
        self.spinBox_x.setObjectName(u"spinBox_x")
        self.spinBox_x.setMaximum(99999)

        self.horizontalLayout_4.addWidget(self.spinBox_x)

        self.label_y = QLabel(self.groupBox_cursorPosition)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setMaximumSize(QSize(15, 16777215))
        self.label_y.setFont(font)
        self.label_y.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_y)

        self.spinBox_y = QSpinBox(self.groupBox_cursorPosition)
        self.spinBox_y.setObjectName(u"spinBox_y")
        self.spinBox_y.setMaximum(999999)

        self.horizontalLayout_4.addWidget(self.spinBox_y)


        self.verticalLayout_2.addWidget(self.groupBox_cursorPosition)

        self.layout_Setup = QVBoxLayout()
        self.layout_Setup.setObjectName(u"layout_Setup")
        self.layout_startStop = QHBoxLayout()
        self.layout_startStop.setObjectName(u"layout_startStop")
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(0, 45))

        self.layout_startStop.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setEnabled(False)
        self.pushButton_stop.setMinimumSize(QSize(0, 45))

        self.layout_startStop.addWidget(self.pushButton_stop)


        self.layout_Setup.addLayout(self.layout_startStop)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.layout_Setup.addWidget(self.line)

        self.layout_hotkey_info = QHBoxLayout()
        self.layout_hotkey_info.setObjectName(u"layout_hotkey_info")
        self.pushButton_setHotkey = QPushButton(self.centralwidget)
        self.pushButton_setHotkey.setObjectName(u"pushButton_setHotkey")
        self.pushButton_setHotkey.setMinimumSize(QSize(0, 45))
        self.pushButton_setHotkey.setMaximumSize(QSize(16777215, 56))

        self.layout_hotkey_info.addWidget(self.pushButton_setHotkey)

        self.groupBox_info = QGroupBox(self.centralwidget)
        self.groupBox_info.setObjectName(u"groupBox_info")
        self.groupBox_info.setMaximumSize(QSize(16777215, 56))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 5)
        self.label_info = QLabel(self.groupBox_info)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_info)

        self.label_github = QLabel(self.groupBox_info)
        self.label_github.setObjectName(u"label_github")
        self.label_github.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_github)


        self.layout_hotkey_info.addWidget(self.groupBox_info)


        self.layout_Setup.addLayout(self.layout_hotkey_info)


        self.verticalLayout_2.addLayout(self.layout_Setup)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 528, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_clickType.setTitle(QCoreApplication.translate("MainWindow", u"Clicker type", None))
        self.radioButton_normalClicker.setText(QCoreApplication.translate("MainWindow", u"Normal clicker", None))
        self.radioButton_insideClicker.setText(QCoreApplication.translate("MainWindow", u"Inside clicker", None))
        self.label_hwnd.setText(QCoreApplication.translate("MainWindow", u"HWND", None))
        self.groupBox_clickerInterval.setTitle(QCoreApplication.translate("MainWindow", u"Click Interval", None))
        self.label_mins.setText(QCoreApplication.translate("MainWindow", u"mins", None))
        self.label_secs.setText(QCoreApplication.translate("MainWindow", u"secs", None))
        self.label_miliseconds.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.groupBox_clickerOptions.setTitle(QCoreApplication.translate("MainWindow", u"Click options", None))
        self.label_clickButton.setText(QCoreApplication.translate("MainWindow", u"Button", None))
        self.comboBox_clickButton.setItemText(0, QCoreApplication.translate("MainWindow", u"Left", None))
        self.comboBox_clickButton.setItemText(1, QCoreApplication.translate("MainWindow", u"Right", None))
        self.comboBox_clickButton.setItemText(2, QCoreApplication.translate("MainWindow", u"Middle", None))

        self.label_clickType.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.comboBox_clickType.setItemText(0, QCoreApplication.translate("MainWindow", u"Single", None))
        self.comboBox_clickType.setItemText(1, QCoreApplication.translate("MainWindow", u"Double", None))

        self.groupBox_repeat.setTitle(QCoreApplication.translate("MainWindow", u"Click repeat", None))
        self.radioButton_repeat.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.label_repeat.setText(QCoreApplication.translate("MainWindow", u"times", None))
        self.radioButton_repeatUntilStopped.setText(QCoreApplication.translate("MainWindow", u"Repeat until stopped", None))
        self.groupBox_cursorPosition.setTitle(QCoreApplication.translate("MainWindow", u"Cursor position", None))
        self.radioButton_currentLocation.setText(QCoreApplication.translate("MainWindow", u"Current location", None))
        self.radioButton_customLocation.setText("")
        self.pushButton_pickLocation.setText(QCoreApplication.translate("MainWindow", u"Pick location", None))
        self.lable_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"Start (F8)", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop (F8)", None))
        self.pushButton_setHotkey.setText(QCoreApplication.translate("MainWindow", u"Set Hotkey", None))
        self.groupBox_info.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Shadow Clicker", None))
        self.label_github.setText(QCoreApplication.translate("MainWindow", u"Github : Bllare", None))
    # retranslateUi

