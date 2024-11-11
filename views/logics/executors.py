# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/11 17:57 
@Desc    ：
"""
import importlib
import inspect
import traceback

from qtrader.base.base_strategy import BaseStrategy


# 执行选择的策略
def execute_strategy(strategy_dir, strategy_name):
    try:
        module_name = f"{strategy_dir}.{strategy_name}"
        strategy_module = importlib.import_module(module_name)

        # 获取模块中的所有类，并筛选出继承了 BaseStrategy 的类
        strategy_class = None
        for _, cls in inspect.getmembers(strategy_module, inspect.isclass):
            if issubclass(cls, BaseStrategy) and cls is not BaseStrategy:
                strategy_class = cls
                break

        if strategy_class is None:
            print(f"模块 {module_name} 中未找到继承 BaseStrategy 的类")
            return

        strategy_instance = strategy_class()
        strategy_instance.run()
        print(f"策略 {strategy_name} 执行完毕！")

    except Exception as e:
        print("执行策略出错：", e)
        print(traceback.format_exc())
