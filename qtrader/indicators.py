# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 10:43 
@Desc    ：各种指标获取
"""
from typing import List

import numpy as np
import talib

from qtrader.models import Stock


def MA(size: int, kline: List[Stock]) -> list:
    """
    计算简单移动平均线 (SMA)
    Args:
        size: 时间周期，例如20表示20天的移动平均
        kline: 股票K线数据，传入指定k线数据

    Returns: 返回一个一维数组，包含每个时间点的SMA值

    """
    if not kline:
        return []
    # 提取收盘价
    close_array = np.array([item.close for item in kline])
    # 计算简单移动平均
    result = talib.SMA(close_array, timeperiod=size)
    return result.tolist()  # 将NumPy数组转换为普通列表返回


def BOLL(size: int, kline: List[Stock]) -> dict:
    """
    计算布林带 (Bollinger Bands)
    Args:
        size: 时间周期（例如20）
        kline: 股票K线数据，传入指定k线数据

    Returns:返回一个字典 {"upper_band": 上轨数组， "middle_band": 中轨数组， "lower_band": 下轨数组}

    """
    if not kline:
        return {"upper_band": [], "middle_band": [], "lower_band": []}

    # 提取收盘价数据
    close_array = np.array([item.close for item in kline])

    # 计算布林带
    upper_band, middle_band, lower_band = talib.BBANDS(close_array, timeperiod=size, nbdevup=2, nbdevdn=2, matype=0)

    # 返回结果字典
    return {
        "upper_band": upper_band,
        "middle_band": middle_band,
        "lower_band": lower_band
    }


def MACD(fast_period, slow_period, signal_period, kline: List[Stock]) -> dict:
    """

    Args:
        fast_period: 快速均线的周期（常见为12）
        slow_period: 慢速均线的周期（常见为26）
        signal_period: 信号线的周期（常见为9）
        kline: 传入指定k线数据

    Returns:返回一个字典 {'dif': dif数组, 'dea': dea数组, 'macd': macd数组}

    """
    # 检查kline数据是否为空
    if not kline:
        return {'DIF': [], 'DEA': [], 'MACD': []}
    # 提取所有收盘价
    close_array = np.array([item.close for item in kline])  # 假设每个K线是一个列表，收盘价在item[4]位置
    # 使用talib计算MACD
    DIF, DEA, _MACD = talib.MACD(close_array,
                                 fastperiod=fast_period,
                                 slowperiod=slow_period,
                                 signalperiod=signal_period)
    # 返回结果
    return {'DIF': DIF, 'DEA': DEA, 'MACD': _MACD * 2}  # MACD通常是DIF和DEA之差的两倍
