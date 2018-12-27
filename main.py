import requests
import re
"""获取简书七日热门话题"""

# url = "https://www.jianshu.com/trending/weekly?utm_medium=index-banner-s&utm_source=desktop"
# proxies = {
#     "http": "218.108.168.68:82",        # 设置代理地址
# }
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/71.0.3578.98 Safari/537.36"
# }
# test = requests.get(url, headers=headers)
# pattern = re.compile(r'target="_blank"\shref="/p/\w{12}\W{2}(.*?)</a>', re.S)
# x = re.findall(pattern, test.text)
# for i in x:
#     print(str(i).lstrip())


import re
import os
"""
获取QQ音乐热门音乐top300
"""
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
song_begin = 0
file_name = "music.txt"
htmlDome = "html_demo.html"

if os.path.exists(file_name):
    os.remove(file_name)
rank = 1        # 统计排名
page = 1
while song_begin < 300:
    print("正在获取第%s页数据。。。" % page)
    url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?" \
          "tpl=3&page=detail&date=2018_51&topid=26&type=top&song_begin=" + str(song_begin) + \
          "&song_num=30&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8" \
          "&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"

    prseon = requests.get(url, headers=header)
    if os.path.exists(htmlDome):
        pass
    else:
        with open(htmlDome, "a+", encoding='utf-8') as f:
            f.write(prseon.text)
    MusicName = re.compile(r'lbumname\W{3}(.*?)\W{3}a', re.S)
    SingerName = re.compile(r'\Wname\W{3}(.*?)\W{5}[s|i]', re.S)
    musicname = re.findall(MusicName, prseon.text)
    singername = re.findall(SingerName, prseon.text)


    for i in musicname:
        with open(file_name, "a+", encoding="utf-8") as w:
            w.write(str(rank)+"  ")
            w.write(i+"\t\t\t")      # 将歌曲名字写入文件
            w.write(singername[musicname.index(i)])
            w.write("\n")
            rank += 1
    song_begin += 30
    page += 1
print("Done!")

# from pyquery import PyQuery as pq
# url = "https://www.jianshu.com/trending/weekly?utm_medium=index-banner-s&utm_source=desktop"
# proxies = {
#     "http": "218.108.168.68:82",        # 设置代理地址
# }
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/71.0.3578.98 Safari/537.36"
# }
# html = requests.get(url, headers=headers)

# print(html.text)

# doc = pq(html.text)
# print(doc('div'))       # 获取所有div标签

# doc = pq(url="https://www.baidu.com")
# print(doc('title'))