# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 11:45 
@Desc    ：
"""
import akshare as ak
import pandas as pd

from qtrader.models import Stock


class StockMarket:
    @staticmethod
    def stock_list() -> pd.DataFrame:
        """获取沪深A股列表"""
        return ak.stock_zh_a_spot_em()

    @staticmethod
    def kline(symbol: str,
              period: str = "daily",
              start_date: str = "",
              end_date: str = "",
              adjust: str = "qfq") -> list:
        """
        获取历史k线数据
        Args:
            symbol: 股票代码
            period: 周期，period='daily'; choice of {'daily', 'weekly', 'monthly'}
            start_date: 开始日期，start_date='20210301'
            end_date: 结束日期，end_date='20210301'
            adjust: 默认返回不复权的数据; qfq: 返回前复权后的数据; hfq: 返回后复权后的数据

        Returns:

        """
        df = ak.stock_zh_a_hist(symbol, period, start_date, end_date, adjust)
        if df.empty:
            return []

        # Ensure '日期' column exists
        if '日期' not in df.columns:
            raise ValueError("Dataframe does not contain '日期' column")

        # Convert '日期' to datetime
        df['date'] = pd.to_datetime(df['日期'])

        # Convert DataFrame rows to list of Stock Pydantic models
        stock_data_list = [
            Stock(
                date=row['date'].strftime('%Y-%m-%d'),
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