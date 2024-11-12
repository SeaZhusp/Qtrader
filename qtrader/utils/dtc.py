# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/12 18:58 
@Desc    ：
"""
from typing import Type, List

import pandas as pd

from qtrader.models import Stock

COLUMN_MAPPING = {
    '日期': 'date',
    '股票代码': 'code',
    '代码': 'code',
    '名称': 'name',
    '最新价': 'last',
    '开盘': 'open',
    '收盘': 'close',
    '最高': 'high',
    '最低': 'low',
    '成交量': 'volume',
    '成交额': 'turnover',
    '振幅': 'amplitude',
    '涨跌幅': 'percent',
    '涨跌额': 'amount',
    '换手率': 'turnover_rate'
}


def df_to_stock(df, model_cls: Type[Stock]) -> List[Stock]:
    """
    将 DataFrame 转换为指定的 Pydantic 数据结构列表，缺失字段自动填充为 None
    :param df: 输入的 DataFrame
    :param model_cls: 自定义数据结构类（例如 Pydantic 模型）
    :return: List[BaseModel]
    """

    # 如果 DataFrame 为空，直接返回空列表
    if df.empty:
        return []

    df = df.rename(columns=COLUMN_MAPPING)

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # 获取 Pydantic 模型的字段名列表
    model_fields = model_cls.__annotations__.keys()

    # 初始化结果列表
    results = []

    # 遍历 DataFrame 的每一行
    for _, row in df.iterrows():
        # 构建包含所有字段的参数字典，DataFrame 中没有的字段自动填充为 None
        instance_data = {field: row.get(field, None) for field in model_fields}
        # 创建 Pydantic 模型实例
        instance = model_cls(**instance_data)
        results.append(instance)

    return results
