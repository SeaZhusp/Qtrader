# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 10:43
@Desc    ：指标
"""
from typing import List, Dict

import numpy as np
import talib

from qtrader.models import Stock


class Indicators:

    @staticmethod
    def ma(size: int, kline: List[Stock]) -> list:
        """
        计算均线
        :param size: 时间周期，例如20表示20天的移动平均
        :param kline: 股票K线数据，传入指定k线数据
        :return: 返回一个一维数组，包含每个时间点的SMA值
        """
        if not kline:
            return []
        # 提取收盘价
        close_array = np.array([item.close for item in kline])
        # 计算简单移动平均
        result = talib.SMA(close_array, timeperiod=size)
        return result.tolist()  # 将NumPy数组转换为普通列表返回

    @staticmethod
    def boll_band(size: int, kline: List[Stock]) -> dict:
        """
        计算布林带
        :param size: 时间周期（例如20）
        :param kline: 股票K线数据，传入指定k线数据
        :return: 返回一个字典 {"upper_band": 上轨数组， "middle_band": 中轨数组， "lower_band": 下轨数组}
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

    @staticmethod
    def macd(fast_period, slow_period, signal_period, kline: List[Stock]) -> dict:
        """
        计算MACD
        :param fast_period: 快速均线的周期（常见为12）
        :param slow_period: 慢速均线的周期（常见为26）
        :param signal_period: 信号线的周期（常见为9）
        :param kline: 传入指定k线数据
        :return: 返回一个字典 {'dif': dif数组, 'dea': dea数组, 'macd': macd数组}
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

    @staticmethod
    def kdj(fastk_period: int, slowk_period: int, slowd_period: int, kline: List[Stock]) -> Dict[str, np.ndarray]:
        """
        计算KDJ
        :param fastk_period: 快速K的周期
        :param slowk_period: 慢速K的周期
        :param slowd_period: 慢速D的周期
        :param kline: 股票的K线数据，包含高、低、收盘价
        :return: 返回一个字典，包含 'k' 和 'd' 数组，分别表示 K 和 D 值
        """
        kline_length = len(kline)
        high_array = np.zeros(kline_length)
        low_array = np.zeros(kline_length)
        close_array = np.zeros(kline_length)

        # 提取高、低、收盘价
        for t, item in enumerate(kline):
            high_array[t] = item.high  # 最高价
            low_array[t] = item.low  # 最低价
            close_array[t] = item.close  # 收盘价

        # 使用 TALIB 计算 STOCH（KDJ 指标的核心计算方法）
        slowk, slowd = talib.STOCH(
            high_array, low_array, close_array,
            fastk_period=fastk_period,
            slowk_period=slowk_period,
            slowk_matype=0,  # 默认采用简单移动平均
            slowd_period=slowd_period,
            slowd_matype=0  # 默认采用简单移动平均
        )

        # 返回 K 和 D 数组
        return {'k': slowk, 'd': slowd}

    @staticmethod
    def volume(kline: List[Stock]) -> np.ndarray:
        """
        计算成交量
        :param kline: 传入指定k线数据
        :return: 返回一个一维数组
        """
        volume_array = np.array([item.volume for item in kline])
        return volume_array