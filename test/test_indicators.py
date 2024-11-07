# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 16:17 
@Desc    ：
"""
import unittest
from qtrader.market.stock import StockMarket


class TestMA(unittest.TestCase):
    def test_boll(self):
        symbol = '000001'
        StockMarket.kline(symbol)
