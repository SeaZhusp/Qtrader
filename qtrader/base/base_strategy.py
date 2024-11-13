# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/11 18:10 
@Desc    ：
"""
from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError("策略必须实现 `run` 方法")
