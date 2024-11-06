# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 9:07 
@Desc    ：日志输出
"""

import os
import sys

from loguru import logger
from qtrader.utils.tools import dt_to_date_str

LOGGER_FORMAT = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
        + " | <level>{level}</level> | <level>{message}</level>"
)


def init_logger(level: str = 'INFO', log_dir: str = 'logs'):
    level = level.upper()
    if level not in ["TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        level = "INFO"  # default

    # set log level to INFO
    logger.remove()
    logger.add(sys.stdout, format=LOGGER_FORMAT, level=level)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 添加文件日志处理器
    log_file = os.path.join(log_dir, f"log_{dt_to_date_str()}.log")
    logger.add(
        sink=log_file,
        format=LOGGER_FORMAT,
        level=level,
        serialize=False,
        rotation="1 week"  # 例如，可以设置日志文件每周轮换一次
    )
