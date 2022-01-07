import requests
from xml.etree import ElementTree
qq_str = '1203069758'
url_str ='http://www.webxml.com.cn//webservices//qqOnlineWebService.asmx//qqCheckOnline?qqCode=%s'%qq_str
text_str = requests.get(url_str)
text_str.encoding='utf-8'
#解析xml格式内容，将字符串转为特殊的对象


node = ElementTree.XML(text_str.text)
print("node等于",node.text)

tree = ElementTree.fromstring(text_str.content)
print("node2等于",tree.text)