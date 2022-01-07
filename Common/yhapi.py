#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OSCar
# @Time     : 2021/11/5 16:46
# @File     : yhapi.py
# @Project  : myblog
# @Mail     : 1203069758@qq.com
import requests
from xml.etree import ElementTree as ET
import json
import xmltodict

url = "http://127.0.0.1:999/bi/api?action=shareDB&token="
token = "80D4B9499F3FB36E20F5ECD45E2D8FD3"
url2 = url + token
data = {'xmlData': '''<?xml version="1.0" encoding="UTF-8"?>
<info>
<refs>
 <ref>
<path>sharedb</path>
<type>db</type>
 </ref>
</refs>
<identity>
 <ref>
<type>user</type>
<name>a</name>
</ref>
</identity>
</info>
'''
        }
headers = {'content-type': 'application/xml'}

res = requests.post(url2, headers=headers, data=data)
print('res的结果是', res.text)

# resDict = json.loads(res.content,strict=False)

resDict2 = xmltodict.parse(res.text)
# print('resdict等于', resDict)
print('resdict等于', resDict2)
print('resdict类型', type(resDict2))
print('resdict类型', resDict2['results']['result']['level'])
print('resdict类型', resDict2['results']['result']['message'])
