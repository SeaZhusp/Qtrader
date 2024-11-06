# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 10:41 
@Desc    ：数据存储与读取
"""
import csv


def txt_save(content, filename, mode='a'):
    """
    保存数据至txt文件
    Args:
        content: 要保存的内容,必须为string格式
        filename: 文件路径及名称
        mode:

    Returns:

    """
    with open(filename, mode=mode, encoding="utf-8") as file:
        file.write(content + '\n')


def txt_read(filename):
    """
    读取txt文件中的数据
    Args:
        filename: 文件路径、文件名称。

    Returns:返回一个包含所有文件内容的列表，其中元素均为string格式

    """
    with open(filename, encoding="utf-8") as file:
        content = file.readlines()
    for i in range(len(content)):
        content[i] = content[i][:len(content[i]) - 1]
        file.close()
    return content


def save_to_csv_file(data, path):
    with open(path, mode="a", newline='', encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)


def read_csv_file(path):
    data = []
    reader = csv.reader(open(path, encoding="utf-8"))
    for item in reader:
        data.append(item)
    return data
