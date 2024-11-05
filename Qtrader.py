# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/5 23:29 
@Desc    ：
"""
import sys

import qdarkstyle
from PySide6.QtWidgets import QApplication

from views.main_view import MainView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    main_view = MainView()
    main_view.show()
    sys.exit(app.exec())
