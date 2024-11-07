# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 23:22 
@Desc    ：
"""
from views.utils.tools import FileTool


class StockInit:

    @staticmethod
    def select_strategies():
        """初始化股票策略"""
        FileTool.list_py_files('')

    @staticmethod
    def market_boards():
        """初始化股票板块"""
        pass


class StrategyInit:

    @staticmethod
    def strategies():
        pass
