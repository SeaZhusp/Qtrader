# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/7 14:31 
@Desc    ：
"""
import unittest
from qtrader.market.stock import StockMarket


class TestQtraderMarketStock(unittest.TestCase):

    def test_kline(self):
        kline = StockMarket.kline('600519', start_date='20241001', end_date='20241031')
