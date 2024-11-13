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
    def fetch_data(sql: str, *args):
        conn = Sqlite3Manager.create_conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            return result
        except Exception as e:
            logger.error(f"SQL error! SQL: {sql}, Args: {args}, Error: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def fetch_one(sql: str, *args):
        conn = Sqlite3Manager.create_conn()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
            return result
        except Exception as e:
            logger.error(f"SQL error! SQL: {sql}, Args: {args}, Error: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def item_to_table(table_name: str, item: Dict[str, Any]):
        conn = Sqlite3Manager.create_conn()
        cursor = conn.cursor()
        sql = ""
        values = []
        try:
            fields = list(item.keys())
            values = list(item.values())
            fields = [f'`{field}`' for field in fields]
            field_str = ','.join(fields)
            val_str = ','.join(['?'] * len(item))
            sql = f"INSERT INTO {table_name} ({field_str}) VALUES({val_str})"
            cursor.execute(sql, values)
            conn.commit()
            return cursor.lastrowid

        except Exception as e:
            conn.rollback()
            logger.error(f"SQL error! SQL: {sql}, Values: {values}, Error: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert_table(table_name: str, item: Dict[str, Any]):
        conn = Sqlite3Manager.create_conn()
        cursor = conn.cursor()
        sql = ""
        values = []
        try:
            fields = list(item.keys())
            values = list(item.values())
            fields = [f'`{field}`' for field in fields]
            field_str = ','.join(fields)
            val_str = ','.join(['?'] * len(item))
            sql = f"INSERT INTO {table_name} ({field_str}) VALUES({val_str})"
            cursor.execute(sql, values)
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            logger.error(f"SQL error! SQL: {sql}, Values: {values}, Error: {e}")
        finally:
            cursor.close()
            conn.close()
