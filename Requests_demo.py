# -*- coding:utf-8 -*-
# !/usr/bin/env python3
"""
Author     : Alexis
Email      : liub@midu.com
ProjectName: Reptile
Flie       : Requests_demo.py
Time       : 2018-12-26 23:11
"""

import requests
r = requests.get("https://baidu.com")
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)