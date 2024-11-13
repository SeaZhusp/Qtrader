# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 11:28 
@Desc    ：
"""
from qtrader.market.stock import StockMarket
from qtrader import BaseStrategy, Indicators, TimeTool


class MoveAvgGoldenCross(BaseStrategy):
    strategy_name = "均线金叉策略"

    def __init__(self):
        super().__init__()
        period = 30
        self.now = TimeTool.dt_to_str()
        self.last_3_day = TimeTool.dt_to_str(delta_day=-period)

    def run(self):
        stock_list = StockMarket.hsj_stocks()
        stock_pool = []
        for code in stock_list['代码']:
            kline = StockMarket.kline(code, 'daily', self.last_3_day, self.now, 'qfq')
            if len(kline) < 30:
                continue
            ma5 = Indicators.ma(5, kline)
            ma10 = Indicators.ma(10, kline)

            if ma5[-1] > ma10[-1] and ma5[-2] <= ma10[-2]:
                stock_pool.append(code)
                print(ma5)
            if stock_pool:
                break
        print(stock_pool)


if __name__ == '__main__':
    MoveAvgGoldenCross().run()