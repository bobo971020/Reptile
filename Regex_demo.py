import re

str = "Hello, my phone number is 010-86432100 and email is liubo98278@qq.com and adderss is https://www.test123.com,zxc@qq.com"


r = re.match("^Hello.\s\w{2}\s", str)
print(r)

r = re.search(r'\d{3}-\d{8}', str)
print(r.group())

r = re.findall(r'\w+@\w+.\w{3}', str)
print(r)

