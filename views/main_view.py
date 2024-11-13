# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/5 23:36 
@Desc    ：
"""
from PySide6.QtWidgets import QMainWindow

from views.ui_desiners.ui_main import Ui_Main


class MainView(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init_values()

    def init_values(self):
        self.statusbar.showMessage('欢迎使用智能量化研究平台！')

    def init_connect(self):
        pass
