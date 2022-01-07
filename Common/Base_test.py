import requests
from Logs.log import log1
import json

class ApiRequest(object):
    # -----第一种请求方式封装request库，调用可根据实际情况传参
    def send_requests(self, method, url, data=None, params=None, headers=None, cookies=None, json=None, files=None,
                      timeout=None):
        self.res = requests.request(method, url, data=data, params=params, headers=headers, cookies=cookies, json=json,
                                  files=files, timeout=timeout)
        return self.res


    def getdict(self, dict1, obj, default=None):
        ''' 遍历嵌套字典，得到想要的value
            dict1所需遍历的字典
            obj 所需value的键'''
        for k, v in dict1.items():
            if k == obj:
                return v
            else:
                if type(v) is dict:  # 如果是字典
                    re = self.getdict(v, obj, default)  # 递归
                    if re is not default:
                        return re

    def get_header(self, headers):
        '''
        将从浏览器复制过来的headers转换成字典
        '''
        headers = dict([line.split(": ", 1) for line in headers.split("\n")])
        return headers

# c='''Connection: keep-alive
# Content-Length: 110
# Pragma: no-cache
# Cache-Control: no-cache
# Accept: application/json, text/plain, */*
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
# Content-Type: application/json;charset=UTF-8
# Origin: http://172.25.16.6:8090
# Referer: http://172.25.16.6:8090/
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9'''
# headers = dict([line.split(": ", 1) for line in c.split("\n")])
# print(headers)
