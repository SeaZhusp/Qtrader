# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 10:42 
@Desc    ：模型
"""
from typing import Optional

from pydantic import BaseModel


class Stock(BaseModel):
    """ 实时行情数据"""
    date: Optional[str] = None  # 交易日
    symbol: Optional[str] = None  # 股票代码
    name: Optional[str] = None  # 股票名称
    last: Optional[float] = None  # 当前价格
    open: Optional[float] = None  # 开盘价
    close: Optional[float] = None  # 收盘价
    high: Optional[float] = None  # 今日最高价
    low: Optional[float] = None  # 今日最低价
    volume: Optional[int] = None  # 成交量
    turnover: Optional[float] = None  # 成交额
    amplitude: Optional[float] = None  # 振幅
    percent: Optional[float] = None  # 涨跌幅
    amount: Optional[float] = None  # 涨跌额
    turnover_rate: Optional[float] = None  # 换手率
