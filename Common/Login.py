# -*- coding: utf-8 -*-
# @Time : 2021-5-7 19:25
# @Author : 奥斯卡
# @Email : 1203069758@qq.com
# @File : Login.py
import requests
import re


class cookie():
    def __init__(self):
        '''这里登录用的账号密码是zzzfwld/12345678Aa'''
        self.url = "http://localhost:999/bi/api?action=login"
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.data = {'adminv': 'admin', 'passv': 'g5'}
        self.request = requests.session()

    def login(self):
        '''
        :return: 这一步是登录，返回登录成功的cookies.后面的操作拿到cookies,就能直接操作接口了
        '''
        # 先获取拼接到的的data和cookies。因为创建session的时候需要cookie
        # 使用旧cookie登录，然后得到登录后的新cookie
        # 使用新cookie就可以操作接口
        res = self.request.post(self.url, headers=self.headers, data=self.data)
        token = re.search('<message>(.*?)</message>', res.text, re.M | re.I)
        # print("token值等于", token.group(1))
        token = token.group(1)
        return token


# r = cookie().login()
