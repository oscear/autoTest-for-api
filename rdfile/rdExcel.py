#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OSCar
# @Time     : 2021/11/5 18:53
# @File     : rdExcel.py
# @Project  : myblog
# @Mail     : 1203069758@qq.com

import xlrd
import getcwd
import os

path = getcwd.get_cwd()

class read_excel():

    def __init__(self, xls, sheet):
        '''
        @param xls: 传入excel的名字
        @param sheet: 传入sheet的名字，注意大小写
        '''
        self.excelpath = os.path.join(path, 'data/' + xls)
        # 打开excel
        self.book = xlrd.open_workbook(self.excelpath)
        # 获取excel
        self.sheet = self.book.sheet_by_name(sheet)

    # 以列表形式读取出所有数据
    def getExceldatas(self):
        data = []
        title = self.sheet.row_values(0)
        # 0获取第一行也就是表头
        print("用例总条数为", self.sheet.nrows)
        for row in range(0, self.sheet.nrows):  # 从第一行包括表头开始获取
            row_value = self.sheet.row_values(row)
            data.append(dict(zip(title, row_value)))  # 将读取出每一条用例作为一个字典存放进列表
        return data


    def get_nrows(self):
        '''获取列表行数'''
        return self.sheet.nrows



# hc = OperationExcel('a.xls','Sheet1')
# print(hc.getExceldatas())
# print(type(hc.getExceldatas()))
# print()
#
# for i in range(1, hc.get_nrows()):
#     num = i - 1
#     print('num的顺序为', num)
#     host = hc.getExceldatas()[num]['Host']
#     print(host)