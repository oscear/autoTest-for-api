# -*- coding: utf-8 -*-
# @Time : 2021-4-2 17:02
# @Author : 奥斯卡
# @Email : 1203069758@qq.com
# @File : Readini.py
import configparser
import os
import getcwd


path = getcwd.get_cwd()


def read_ini(section, name):
    rf = configparser.ConfigParser()
    inipath = os.path.join(path, 'Config/conf.ini')
    # rf.read("..\Config\conf.ini")
    rf.read(inipath)
    key = rf.get(section, name)
    return key



