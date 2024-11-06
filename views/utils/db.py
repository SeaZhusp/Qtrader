# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 23:28 
@Desc    ：
"""
import sqlite3
from typing import Dict, Any

from loguru import logger


class Sqlite3Manager:

    @staticmethod
    def create_conn():
        return sqlite3.connect('database.db')

    @staticmethod
    def fetch_data(sql, *args):
        conn = Sqlite3Manager.create_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, *args)
            result = cursor.fetchall()
            return result
        except Exception as e:
            logger.error(f" sql error! because: {e}")
        finally:
            conn.close()

    @staticmethod
    def fetch_one(sql, *args):
        conn = Sqlite3Manager.create_conn()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, *args)
            result = cursor.fetchone()
            return result
        except Exception as e:
            logger.error(f" sql error! because: {e}")
        finally:
            conn.close()

    @staticmethod
    def item_to_table(table_name: str, item: Dict[str, Any]):
        conn = Sqlite3Manager.create_conn()
        try:
            cursor = conn.cursor()
            fields = list(item.keys())
            values = list(item.values())
            fields = [f'{field}' for field in fields]
            field_str = ','.join(fields)
            val_str = ','.join(['?'] * len(item))
            sql = "INSERT INTO %s (%s) VALUES(%s)" % (table_name, field_str, val_str)
            cursor.execute(sql, values)
            conn.commit()  # 提交事务
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            logger.error(f" sql error! because: {e}")
        finally:
            conn.close()
