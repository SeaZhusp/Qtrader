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
        print(df)
        if df.empty:
            return []

        # Ensure '日期' column exists
        if '日期' not in df.columns:
            raise ValueError("Dataframe does not contain '日期' column")

        # Convert DataFrame rows to list of Stock Pydantic models
        stock_data_list = [
            Stock(
                date=row['日期'].strftime('%Y-%m-%d'),
                symbol=row['股票代码'],
                open=row['开盘'],
                close=row['收盘'],
                high=row['最高'],
                low=row['最低'],
                volume=row['成交量'],
                turnover=row['成交额'],
                amplitude=row['振幅'],
                percent=row['涨跌幅'],
                amount=row['涨跌额'],
                turnover_rate=row['换手率']
            )
            for _, row in df.iterrows()
        ]
        return stock_data_list
