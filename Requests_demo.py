# -*- coding:utf-8 -*-
# !/usr/bin/env python3
"""
Author     : Alexis
Email      : liub@midu.com
ProjectName: Reptile
Flie       : Requests_demo.py
Time       : 2018-12-26 23:11
"""


"基本使用"
import requests
# r = requests.get("https://baidu.com")
# print(type(r))      # 输出返回类型
# print(r.status_code)    # 打印状态码
# print(type(r.text))     # 打印文本类型
# print(r.text)       # 输出文本
# print(r.cookies)    # 输出cookie
#
# print(requests.post("http://httpbin.org/post"))
# print(requests.put("http://httpbin.org/put"))
# print(requests.delete("http://httpbin.org/delete"))
# print(requests.head("http://httpbin.org/get"))
# print(requests.options("http://httpbin.org/get"))

# r = requests.get('http://httpbin.org/get')
# print(r.text)

# data ={
#     'name': "germey",
#     'age': 22
# }

# r = requests.get("http://httpbin.org/get", params=data)     # 添加参数
# print(r.text)
# # print(type(r.text))
# print(type(r.json()))

"获取知乎探索"
# import re
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# title = re.findall(pattern, r.text)
# for i in title:
#     print(i)

"获取GitHub icon保存"
# r = requests.get("https://github.com/favicon.ico")
# with open("test.ico", "wb") as f:
#     f.write(r.content)

"上传文件"
# import requests
# file = {"file": (open("test.ico", "rb"))}
# r = requests.post("http://httpbin.org/post",data=file)
# print(r.text)

"获取cookie"
# import requests
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key+"="+value)

"SSL证书验证"
# import logging
# import requests
# logging.captureWarnings(True)       # 捕捉警告并忽略
# r = requests.get("https://www.12306.cn", verify=False)  # 跳过证书
# print(r.status_code)
# "指定证书"
# # x = requests.get("https://www.12306.cn", cart=('path/server.crt', 'path/key'))  # 指定证书文件，包括证书和密钥

"代理设置"
import json
# proxies={
#     # "http": "119.101.113.130:9999",
# }
#
# r = requests.get("https://www.baidu.com", proxies=proxies)
# print(r)
# print(r.headers)
# print(type(r))

