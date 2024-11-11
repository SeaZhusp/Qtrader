# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 11:28 
@Desc    ：
"""
from qtrader.market.stock import StockMarket
from qtrader.factors import Indicators
from qtrader.base.base_strategy import BaseStrategy


class MoveAvgGoldenCross(BaseStrategy):
    def __init__(self):
        pass

    def run(self):
        stock_list = StockMarket.hsj_stocks()
        stock_pool = []
        for symbol in stock_list['代码']:
            kline = StockMarket.kline(symbol, 'daily', '20240101', '20241105', 'qfq')
            if len(kline) < 30:
                continue
            ma5 = Indicators.ma(5, kline)
            ma10 = Indicators.ma(10, kline)

            if ma5[-1] > ma10[-1] and ma5[-2] <= ma10[-2]:
                stock_pool.append(symbol)
                print(ma5)
            if stock_pool:
                break
        print(stock_pool)


if __name__ == '__main__':
    MoveAvgGoldenCross().run()
