# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKGuWoL.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QHeaderView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(955, 600)
        self.action = QAction(Main)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(Main)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 131, 51))
        self.startTime = QDateEdit(self.groupBox)
        self.startTime.setObjectName(u"startTime")
        self.startTime.setGeometry(QRect(10, 20, 110, 22))
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(160, 10, 131, 51))
        self.endTime = QDateEdit(self.groupBox_2)
        self.endTime.setObjectName(u"endTime")
        self.endTime.setGeometry(QRect(10, 20, 110, 22))
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(310, 10, 171, 51))
        self.StrategyList = QComboBox(self.groupBox_3)
        self.StrategyList.setObjectName(u"StrategyList")
        self.StrategyList.setGeometry(QRect(10, 20, 101, 22))
        self.btnloadStrategy = QPushButton(self.groupBox_3)
        self.btnloadStrategy.setObjectName(u"btnloadStrategy")
        self.btnloadStrategy.setGeometry(QRect(120, 20, 41, 23))
        self.btnSelectStock = QPushButton(self.tab)
        self.btnSelectStock.setObjectName(u"btnSelectStock")
        self.btnSelectStock.setGeometry(QRect(500, 22, 81, 31))
        self.stockPool = QTableWidget(self.tab)
        self.stockPool.setObjectName(u"stockPool")
        self.stockPool.setGeometry(QRect(10, 70, 911, 421))
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
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action)

        self.retranslateUi(Main)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Qtrader", None))
        self.action.setText(QCoreApplication.translate("Main", u"\u5173\u4e8e", None))
        self.action_2.setText(QCoreApplication.translate("Main", u"\u53c2\u6570\u914d\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Main", u"\u5f00\u59cb\u65e5\u671f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Main", u"\u7ed3\u675f\u65e5\u671f", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Main", u"\u7b56\u7565\u9009\u62e9", None))
        self.btnloadStrategy.setText(QCoreApplication.translate("Main", u"\u5237\u65b0", None))
        self.btnSelectStock.setText(QCoreApplication.translate("Main", u"\u5f00\u59cb\u9009\u80a1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Main", u"\u7b56\u7565\u9009\u80a1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Main", u"\u80a1\u7968\u56de\u6d4b", None))
        self.menu.setTitle(QCoreApplication.translate("Main", u"\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("Main", u"\u5e2e\u52a9", None))
    # retranslateUi

