# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 23:22 
@Desc    ：
"""
import importlib
import traceback

from qtrader import FileTool, BaseStrategy


class StrategyInit:

    @staticmethod
    def stock_selection_strategies():
        """初始化策略"""
        strategies = []
        strategy_path = FileTool.join_path(FileTool.get_root_path(), 'strategies', 'select_stock')
        files = FileTool.list_py_files(strategy_path)
        for file in files:
            module_name = file[:-3]
            module_path = f"strategies.select_stock.{module_name}"
            try:
                # 动态导入模块
                strategy_module = importlib.import_module(module_path)
                # 查找继承了 BaseStrategy 的类
                for _, cls in strategy_module.__dict__.items():
                    if isinstance(cls, type) and issubclass(cls, BaseStrategy) and cls is not BaseStrategy:
                        # 检查 `strategy_name` 是否定义
                        strategy_name = getattr(cls, 'strategy_name', None)
                        if strategy_name:
                            strategies.append(strategy_name)
                        else:
                            raise ValueError(f"策略类 {cls.__name__} 未定义 `strategy_name` 属性")
            except Exception as e:
                print(f"加载策略模块 {module_name} 时出错：{e}")
                print(traceback.format_exc())
        return strategies
