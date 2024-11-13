# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/7 10:32
@Desc    ：
"""
import os
import time
import decimal
import datetime
from pathlib import Path


class FileTool:
    @staticmethod
    def get_root_path():
        return os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))

    @staticmethod
    def join_path(root_path, *path):
        return os.path.join(root_path, *path)

    @staticmethod
    def is_valid_path(path: str) -> bool:
        """判断路径是否存在且是文件"""
        return os.path.exists(path)

    @staticmethod
    def is_directory(path: str) -> bool:
        """判断路径是否是一个目录"""
        return os.path.isdir(path)

    @staticmethod
    def is_file(path: str) -> bool:
        """判断路径是否是一个文件"""
        return os.path.isfile(path)

    @staticmethod
    def list_py_files(directory: str, recursive: bool = False, return_full_path: bool = False) -> list:
        """
        列出指定目录下所有的 .py 文件，排除 __init__.py 文件
        :param directory:指定目录
        :param recursive:是否递归查找子目录，默认为 False。
        :param return_full_path:是否返回完整路径，默认为 False，表示只返回文件名。
        :return:
        """
        if recursive:
            py_files = [file if return_full_path else file.name
                        for file in Path(directory).rglob("*.py")
                        if file.name != "__init__.py"]
        else:
            py_files = [file if return_full_path else file.name
                        for file in Path(directory).glob("*.py")
                        if file.name != "__init__.py"]

        return py_files


class TimeTool:
    @staticmethod
    def sleep(seconds: int):
        time.sleep(seconds)

    @staticmethod
    def get_current_timestamp(str_len: int = 10) -> int:
        """获取当前时间戳"""
        if isinstance(str_len, int) and 0 < str_len < 17:
            return int(str(time.time()).replace(".", "")[:str_len])
        raise Exception("timestamp length can only between 0 and 16.")

    @staticmethod
    def ts_to_utc_str(ts=None, fmt='%Y-%m-%dT%H:%M:%S.000z') -> str:
        """将时间戳转换为UTC时间格式，'2020-07-25T03:05:00.000z'"""
        if not ts:
            ts = TimeTool.get_current_timestamp()
        dt = datetime.datetime.utcfromtimestamp(int(ts))
        return dt.strftime(fmt)

    @staticmethod
    def get_datetime(fmt='%Y%m%d%H%M%S'):
        """ 获取日期时间字符串，包含 年 + 月 + 日 + 时 + 分 + 秒 """
        today = datetime.datetime.today()
        str_dt = today.strftime(fmt)
        return str_dt

    @staticmethod
    def str_to_dt(date_str=None, fmt='%Y%m%d', delta_day=0):
        """日期字符串转换到datetime对象"""
        if not date_str:
            dt = datetime.datetime.today()
        else:
            dt = datetime.datetime.strptime(date_str, fmt)
        if delta_day:
            dt += datetime.timedelta(days=delta_day)
        return dt

    @staticmethod
    def dt_to_str(dt=None, fmt='%Y%m%d', delta_day=0):
        """datetime对象转换到日期字符串"""
        if not dt:
            dt = datetime.datetime.today()
        if delta_day:
            dt += datetime.timedelta(days=delta_day)
        str_d = dt.strftime(fmt)
        return str_d

    @staticmethod
    def get_utc_time():
        """ 获取当前utc时间 """
        utc_t = datetime.datetime.utcnow()
        return utc_t

    @staticmethod
    def get_localtime():
        """ 获取本地时间 """
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return localtime

    @staticmethod
    def ts_to_datetime_str(ts=None, fmt='%Y-%m-%d %H:%M:%S'):
        """将时间戳转换为日期时间格式，年-月-日 时:分:秒"""
        if not ts:
            ts = TimeTool.get_current_timestamp()
        dt = datetime.datetime.fromtimestamp(int(ts))
        return dt.strftime(fmt)

    @staticmethod
    def datetime_str_to_ts(dt_str, fmt='%Y-%m-%d %H:%M:%S'):
        """将日期时间格式字符串转换成时间戳"""
        ts = int(time.mktime(datetime.datetime.strptime(dt_str, fmt).timetuple()))
        return ts

    @staticmethod
    def datetime_to_timestamp(dt=None, tzinfo=None):
        """将datetime对象转换成时间戳"""
        if not dt:
            dt = TimeTool.get_utc_time()
        if not tzinfo:
            tzinfo = datetime.timezone.utc
        ts = int(dt.replace(tzinfo=tzinfo).timestamp())
        return ts

    @staticmethod
    def utctime_str_to_ts(utctime_str, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
        """将UTC日期时间格式字符串转换成时间戳
        """
        dt = datetime.datetime.strptime(utctime_str, fmt)
        timestamp = int(dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp())
        return timestamp

    @staticmethod
    def float_to_str(f, p=20):
        """将给定的float转换为字符串，而无需借助科学计数法。"""
        if isinstance(f, str):
            f = float(f)
        ctx = decimal.Context(p)
        d1 = ctx.create_decimal(repr(f))
        return format(d1, 'f')

    @staticmethod
    def now():
        """获取当前的小时和分钟信息，返回字符串，例如："02:47"，可以用来在每日早上去查询一下今日是否开盘"""
        localtime = TimeTool.get_localtime()
        result = localtime.split(" ")[1]
        t = result[0: 5]
        return t

    @staticmethod
    def is_open_time() -> bool:
        """是否A股交易时间，返回例如“200”，表示当前为02：00"""
        t = TimeTool.now()
        result = int(t.replace(":", ""))
        if 930 <= result <= 1130 or 1300 <= result <= 1500:
            return True
        else:
            return False