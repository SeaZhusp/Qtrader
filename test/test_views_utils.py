# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/7 10:54 
@Desc    ：
"""
import unittest
from qtrader.utils import FileTool


class TestViewsUtilsTools(unittest.TestCase):

    def test_file_tool(self):
        root_path = FileTool.get_root_path()
        self.assertIn('Qtrader', root_path)
        self.assertTrue(FileTool.is_directory(root_path) is True)
        py_files = FileTool.list_py_files(root_path)
        self.assertIn('Qtrader.py', py_files)
