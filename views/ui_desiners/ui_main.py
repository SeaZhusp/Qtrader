# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainHAioZo.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGroupBox, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(955, 600)
        icon = QIcon()
        icon.addFile(u":/images/images/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Main.setWindowIcon(icon)
        self.action = QAction(Main)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(Main)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(Main)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.startTime = QDateEdit(self.groupBox)
        self.startTime.setObjectName(u"startTime")
        self.startTime.setMinimumSize(QSize(0, 26))

        self.verticalLayout_2.addWidget(self.startTime)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.endTime = QDateEdit(self.groupBox_2)
        self.endTime.setObjectName(u"endTime")
        self.endTime.setMinimumSize(QSize(0, 26))

        self.verticalLayout_3.addWidget(self.endTime)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 26))

        self.verticalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_6.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.StrategyList = QComboBox(self.groupBox_3)
        self.StrategyList.setObjectName(u"StrategyList")
        self.StrategyList.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.StrategyList)


        self.verticalLayout_6.addWidget(self.groupBox_3)

        self.btnSelectStock = QPushButton(self.tab)
        self.btnSelectStock.setObjectName(u"btnSelectStock")
        self.btnSelectStock.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.btnSelectStock)

        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 26))
        self.checkBox.setChecked(False)

        self.verticalLayout_6.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.tab)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(0, 26))
        self.checkBox_2.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBox_2)

        self.progressBar = QProgressBar(self.tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 26))
        self.progressBar.setValue(24)

        self.verticalLayout_6.addWidget(self.progressBar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stockPool = QTableWidget(self.groupBox_6)
        self.stockPool.setObjectName(u"stockPool")

        self.verticalLayout_7.addWidget(self.stockPool)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 955, 20))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action)
        self.menu_3.addAction(self.action_3)

        self.retranslateUi(Main)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Qtrader - \u667a\u80fd\u91cf\u5316\u7814\u7a76\u5de5\u5177", None))
        self.action.setText(QCoreApplication.translate("Main", u"\u5173\u4e8e", None))
        self.action_2.setText(QCoreApplication.translate("Main", u"\u53c2\u6570\u914d\u7f6e", None))
        self.action_3.setText(QCoreApplication.translate("Main", u"\u80a1\u7968\u6570\u636e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Main", u"\u5f00\u59cb\u65e5\u671f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Main", u"\u7ed3\u675f\u65e5\u671f", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Main", u"\u677f\u5757", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Main", u"\u7b56\u7565", None))
        self.btnSelectStock.setText(QCoreApplication.translate("Main", u"\u5f00\u59cb\u9009\u80a1", None))
        self.checkBox.setText(QCoreApplication.translate("Main", u"\u9009\u80a1\u524d\u6e05\u9664\u80a1\u7968\u6c60", None))
        self.checkBox_2.setText(QCoreApplication.translate("Main", u"\u53d1\u9001\u9489\u9489\u63d0\u9192\uff08\u9700\u8981\u5148\u914d\u7f6e\uff09", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Main", u"\u80a1\u7968\u6c60", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Main", u"\u7b56\u7565\u9009\u80a1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Main", u"\u80a1\u7968\u56de\u6d4b", None))
        self.menu.setTitle(QCoreApplication.translate("Main", u"\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("Main", u"\u5e2e\u52a9", None))
        self.menu_3.setTitle(QCoreApplication.translate("Main", u"\u6570\u636e\u7ba1\u7406", None))
    # retranslateUi

