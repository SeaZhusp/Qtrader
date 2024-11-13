# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/7 10:32 
@Desc    ：
"""
import os
from pathlib import Path


class FileTool:
    @staticmethod
    def get_root_path():
        return os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))

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
