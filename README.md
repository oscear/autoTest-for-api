Python-Requests-PyTest-Excel-Allure

#### 目录说明
- **common**
  公用的基础方法，连接数据库执行SQL语句、获取多层嵌套dict中某一个key的值等
- **config**
  存放配置文件
- **Data**
  存放测试用户和测试相关数据
- **Logs**
  存放日志
- **test_pytest**
  测试用例执行目录，里面只写具体的测试用例代码，测试用例要以test_开头或者以_test结尾，测试用例不改变的情况下，这里面的代码编写好后一般不需要进行修改
- **rdFile**
  读取各类文件,目前只包含有excel、ini，后续扩充
- **conftest.py**
  与conftest.py同目录的文件执行时都会执行该文件
  目前创建driver对象和运行失败截图的放在此文件中的
* **Report**
  保存运行结果的目录，用的是allure来生成的报告，多个json文件：
  也可通过jenkins集成allure报告，可看到执行结果的趋势
