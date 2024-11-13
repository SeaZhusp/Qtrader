# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 11:45 
@Desc    ：
"""
from typing import List

import akshare as ak
import pandas as pd

from qtrader.models import Stock
from qtrader.utils.dtc import df_to_stock_list


class StockMarket:
    """东方财富股票市场数据"""

    @staticmethod
    def hsj_stocks() -> pd.DataFrame:
        """获取 沪深京 A股列表"""
        return ak.stock_zh_a_spot_em()

    @staticmethod
    def boards() -> pd.DataFrame:
        """获取板块"""
        return ak.stock_board_industry_name_em()

    @staticmethod
    def board_stocks(symbol: str = '小金属') -> pd.DataFrame:
        """
        获取板块成分股
        :param symbol: 查询的板块名，名称来源于：StockMarketEM.boards()
        :return:
        """
        return ak.stock_board_industry_cons_em(symbol)

    @staticmethod
    def kline(code: str,
              period: str = "daily",
              start_date: str = "",
              end_date: str = "",
              adjust: str = "qfq") -> List[Stock]:
        """
        获取股票的K线
        :param code: 股票代码
        :param period: 周期，period='daily'; choice of {'daily', 'weekly', 'monthly'}
        :param start_date: 开始日期，start_date='20210301'
        :param end_date: 结束日期，end_date='20210301'
        :param adjust: 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据
        :return:
        """
        df = ak.stock_zh_a_hist(code, period, start_date, end_date, adjust)
        return df_to_stock_list(df, Stock)
