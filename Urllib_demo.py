# -*- coding:utf-8 -*-

import urllib

"获取百度页面的源码"
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))


# respose = urllib.request.urlopen("https://www.python.org")
# print(type(respose))
# print(respose.status)             # 获取状态码
# print(respose.getheaders())
# print(respose.getheader('Server')) # 获取服务器类型
# print(respose.read().decode('utf-8'))

"data参数的使用"
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

"模拟POST请求"
# from urllib import request, parse
# url = 'http://httpbin.org/post'
# headers = {
#     'User-agent': 'Mozilla/4.0(compatible; MSIE 5.5 Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {'dictname': 'Germey'}
# data = bytes(parse.urlencode(dict), encoding='utf8')              # 通过bytes转换称字节
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response. read().decode('utf-8'))

" 获取cookie "
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for itme in cookie:
#     print(itme.name+"="+itme.value)

"保存Cookie到文档"
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)

"另一种格式保存Cookie到文档"
# filename = 'LWPcookies.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)

"Request使用"
# request = urllib.request.Request("http://www.baidu.com")
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
# print(dir(response))

"代理配置"
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
# proxy_handler = ProxyHandler({
#     'http': 'http://119.101.113.235:9999',  # https://www.kuaidaili.com/free/inha/  免费代理ip地址
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open("http://www.baidu.com", timeout=6)
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

"异常处理"
# from urllib import request, error
#
# try:
#     response = request.urlopen('http://www.baidu.com')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep="\n")
# except error.URLError as e:
#     print(e.reason)
# else:
#     print("Request Successfully")

# import socket
# import urllib.error
#
# try:
#     response = urllib.request.urlopen("https://www.baidu.com", timeout=0.01)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print("Time Out")

"URL解析"
# from urllib.parse import urlparse
# url = 'http://www.baidu.com/index.html;user?id=5#commit'
# result = urlparse(url)
# print(type(result), result)     # 简介格式：scheme://netloc/path;params?query*fragment

# result = urllib.parse.urlparse(url="www.baidu.com", scheme="",allow_fragments="https")
# print(result)

"URL构造"
# result = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urllib.parse.urlunparse(result))  # 接受一个可迭代对象，长度必须是6
# result = urllib.parse.urlsplit(url)
# print(result)   # 功能与urlparse一致，只返回5个结果，不解析params（参数）部分

"URL连接"
# from urllib.parse import urljoin
# print(urljoin("www.baidu.com", "https://www.baidu.com"))
# print(urljoin("http://www.baidu.com", "index.html"))

"urlencode方法"
# from urllib.parse import urlencode
# params = {
#     'name': 'liubo',
#     'age': 22
# }
# base_url = "http://www.baidu.com?"
# url = base_url + urlencode(params)    # 将一个参数字典序列化
# print(url)

# from urllib.parse import quote
# from urllib.parse import unquote
# keyword = '壁纸'
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)    # 将中文转化为URL编码
# print(url)
# print(unquote(url))     # 将URL编码转化为中文

"分析robots协议"
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url("https://www.jianshu.com/robots.txt")
rp.read()
print(rp.can_fetch("*", "https://www.jianshu.com/p/d8b31d20a867"))      # 返回TURE或FLASE



