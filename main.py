import requests
import re
"""获取简书七日热门话题"""

url = "https://www.jianshu.com/trending/weekly?utm_medium=index-banner-s&utm_source=desktop"
proxies = {
    "http": "218.108.168.68:82",        # 设置代理地址
}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/71.0.3578.98 Safari/537.36"
}
test = requests.get(url, headers=headers)
# pattern = re.compile(r'<a\s\w{5}=.+href=".{3}\w{12}".+</a>', re.S)
pattern = re.compile(r'target="_blank"\shref="/p/\w{12}\W{2}(.*?)</a>', re.S)
x = re.findall(pattern, test.text)
for i in x:
    print(str(i).lstrip())