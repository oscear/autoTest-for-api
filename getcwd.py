# -*- coding: utf-8 -*-
# @Time : 2021-4-22 11:27
# @Author : 奥斯卡
# @Email : 1203069758@qq.com
# @File : getcwd.py
import os
def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    #当前文件的绝对路径
    return path

os.getcwd()#获取当前目录
os.path.dirname(__file__)#获取当前目录
os.path.dirname(os.path.dirname(__file__))#获取当前目录的上一级