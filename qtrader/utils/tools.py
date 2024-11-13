# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/5 21:09
@Desc    ：工具包
"""
import datetime
import decimal
import time


def sleep(seconds: int):
    time.sleep(seconds)


def get_current_timestamp(str_len: int = 10) -> int:
    """获取当前时间戳"""
    if isinstance(str_len, int) and 0 < str_len < 17:
        return int(str(time.time()).replace(".", "")[:str_len])
    raise Exception("timestamp length can only between 0 and 16.")


def ts_to_utc_str(ts=None, fmt='%Y-%m-%dT%H:%M:%S.000z') -> str:
    """将时间戳转换为UTC时间格式，'2020-07-25T03:05:00.000z'"""
    if not ts:
        ts = get_current_timestamp()
    dt = datetime.datetime.utcfromtimestamp(int(ts))
    return dt.strftime(fmt)


def get_cur_datetime_m(fmt='%Y%m%d%H%M%S%f'):
    """ 获取当前日期时间字符串，包含 年 + 月 + 日 + 时 + 分 + 秒 + 微秒 """
    today = datetime.datetime.today()
    str_m = today.strftime(fmt)
    return str_m


def get_datetime(fmt='%Y%m%d%H%M%S'):
    """ 获取日期时间字符串，包含 年 + 月 + 日 + 时 + 分 + 秒 """
    today = datetime.datetime.today()
    str_dt = today.strftime(fmt)
    return str_dt


def date_str_to_dt(date_str=None, fmt='%Y%m%d', delta_day=0):
    """日期字符串转换到datetime对象"""
    if not date_str:
        dt = datetime.datetime.today()
    else:
        dt = datetime.datetime.strptime(date_str, fmt)
    if delta_day:
        dt += datetime.timedelta(days=delta_day)
    return dt


def dt_to_date_str(dt=None, fmt='%Y%m%d', delta_day=0):
    """datetime对象转换到日期字符串"""
    if not dt:
        dt = datetime.datetime.today()
    if delta_day:
        dt += datetime.timedelta(days=delta_day)
    str_d = dt.strftime(fmt)
    return str_d


def get_utc_time():
    """ 获取当前utc时间 """
    utc_t = datetime.datetime.utcnow()
    return utc_t


def get_localtime():
    """ 获取本地时间 """
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


def ts_to_datetime_str(ts=None, fmt='%Y-%m-%d %H:%M:%S'):
    """将时间戳转换为日期时间格式，年-月-日 时:分:秒"""
    if not ts:
        ts = get_current_timestamp()
    dt = datetime.datetime.fromtimestamp(int(ts))
    return dt.strftime(fmt)


def datetime_str_to_ts(dt_str, fmt='%Y-%m-%d %H:%M:%S'):
    """将日期时间格式字符串转换成时间戳"""
    ts = int(time.mktime(datetime.datetime.strptime(dt_str, fmt).timetuple()))
    return ts


def datetime_to_timestamp(dt=None, tzinfo=None):
    """将datetime对象转换成时间戳"""
    if not dt:
        dt = get_utc_time()
    if not tzinfo:
        tzinfo = datetime.timezone.utc
    ts = int(dt.replace(tzinfo=tzinfo).timestamp())
    return ts


def utctime_str_to_ts(utctime_str, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """将UTC日期时间格式字符串转换成时间戳
    """
    dt = datetime.datetime.strptime(utctime_str, fmt)
    timestamp = int(dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp())
    return timestamp


def utctime_str_to_mts(utctime_str, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """将UTC日期时间格式字符串转换成时间戳（毫秒）
    """
    dt = datetime.datetime.strptime(utctime_str, fmt)
    timestamp = int(dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None).timestamp() * 1000)
    return timestamp


def float_to_str(f, p=20):
    """将给定的float转换为字符串，而无需借助科学计数法。"""
    if isinstance(f, str):
        f = float(f)
    ctx = decimal.Context(p)
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')


def now():
    """获取当前的小时和分钟信息，返回字符串，例如："02:47"，可以用来在每日早上去查询一下今日是否开盘"""
    localtime = get_localtime()
    result = localtime.split(" ")[1]
    t = result[0: 5]
    return t


def not_open_time() -> bool:
    """获取小时和分钟时间，返回例如“200”，表示当前为02：00，为了在非交易时间进行过滤"""
    t = now()
    result = int(t.replace(":", ""))
    if result < 900 or result > 1500:
        return True
    else:
        return False
