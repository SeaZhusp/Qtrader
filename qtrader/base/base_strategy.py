# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/11 18:10 
@Desc    ：
"""
from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    strategy_name = None

    def __init__(self):
        if not self.strategy_name or not isinstance(self.strategy_name, str):
            raise ValueError("策略类必须定义 `strategy_name` 属性，并且必须是字符串类型")

    @abstractmethod
    def run(self):
        raise NotImplementedError("策略类必须实现 `begin` 方法")
