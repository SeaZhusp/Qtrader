# -*- coding: UTF-8 -*-
"""
@Author  ：秋枫zsp
@Email   ：370172879@qq.com
@Date    ：2024/11/6 10:19 
@Desc    ：钉钉消息发送
"""
import json

import requests
from loguru import logger


class DingTalk:
    def __init__(self, url: str):
        self.url = url

    def text(self, content):
        """推送文本类型信息至钉钉"""
        json_text = {
            "msgtype": "text",
            "at": {
                "atMobiles": [
                    ""
                ],
                "isAtAll": False
            },
            "text": {
                "content": content
            }
        }

        headers = {'Content-Type': 'application/json;charset=utf-8'}
        result = requests.post(self.url, json.dumps(json_text), headers=headers)  # 发送钉钉消息并返回发送结果
        logger.debug("dingtalk send msg result:{} message：{}".format(result, content))
        return result

    def markdown(self, content, title: str = '提醒'):
        """
        推送markdown类型信息至钉钉
        :param content: 消息内容
                            content = "### 订单更新推送\n\n"\
                                       "> **订单ID:** 1096989546123445\n\n"\
                                       "> **订单状态:** FILLED\n\n"\
                                       "> **时间戳:** 2021年1月2日"
        :param title: 消息标题
        :return:
        """
        headers = {'Content-Type': 'application/json'}
        body = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": content
            }
        }
        body = json.dumps(body)
        response = requests.post(self.url, data=body, headers=headers)
        logger.debug("dingtalk send msg result:", response)
        return response
