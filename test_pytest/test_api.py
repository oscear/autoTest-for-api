#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : OSCar
# @Time     : 2021/11/5 17:49
# @File     : test_api.py
# @Project  : apitest
# @Mail     : 1203069758@qq.com
import os
import pytest
from rdfile.rdini import read_ini
from rdfile.rdExcel import read_excel
from Common.Base_test import ApiRequest
from Common.Login import cookie
from Logs.log import log1


class TestYongHong:


    def setup_class(self):
        print('开始测试')


    def teardown_class(self):
        print('结束测试')

    def test_api(self):
        token = cookie().login()
        ip = read_ini('url', 'ip')
        port = read_ini('url', 'port')
        datatable = read_excel('a.xls', 'Sheet1')
        data = datatable.getExceldatas()
        # 读出来是个列表内包含字典

        try:
            # 因为第一行是excel表头，从第二行开始获取
            for i in range(1, datatable.get_nrows()):
                path = data[i]['path']
                method = data[i]['method']
                headers = data[i]['headers']
                body = data[i]['data']
                # 前面是从excel取得值
                url = 'http://' + ip + ':' + port + path + token
                # print('url是', url)
                # 拼接url
                checkpoint = data[i]['check']
                res = ApiRequest().send_requests(method=method, url=url, headers=eval(headers), data=eval(body))
                # print('res等于', res.text)
                log1.info("正在测试的接口编号是:%s,名称是%s" % (data[i]['c_bh'], data[i]['name']))
                assert checkpoint in res.text, '响应内容错误'
        except Exception:
            log1.error("有接口预期不符")


if __name__ == '__main__':
    # os.system(r'del  /f  /q  ..\Logs\ALL_Logs')
    # os.system(r'del  /f  /q  ..\Logs\ERROR_Logs')  # 先删除旧日志
    pytest.main(['-s', '-v', 'test_api.py', '--clean-alluredir', '--alluredir', '../report/allure_result'])
    os.system(r'allure serve ../report/allure_result')
    # 等同于在dos执行：pytest -s -v  --clean-alluredir --alluredir ../report/allure_result
    # 等同于在dos执行： allure serve ../report/allure_result
