import datetime
import json
import re

import os
import requests
import wget
from bs4 import BeautifulSoup as soup
from pprint import pprint
import xml.etree.ElementTree as et
import time

p="http://www.btbttpic.com/upload/attach/000/025/be1af3d63f95c28de1dccd316934f955.jpg"

h="http://www.1btjia.com/attach-dialog-fid-8-aid-73175-ajax-1.htm"
h.strip().endswith('rar')
def extract_content(url):
    '''
    抽取南方周末的报道列表
    '''
    try:
        response = requests.get(url)
    except Exception as e:
        print("Exception: {}".format(e))
        print(url)
        return ""
    else:
        time.sleep(6)
        return response.text

c = extract_content(h)

# c={"servererror":"","status":1,"message":{"width":"400","height":300,"pos":"center","title":"\u9644\u4ef6\u4e0b\u8f7d","body":"\n\n<dl>\n\t<dt>\u9644\u4ef6\u540d\uff1a<\/dt>\n\t<dd><img src=\"\/view\/image\/filetype\/zip.gif\" width=\"16\" height=\"16\" \/> btbtt77.com90\u540e\u65e5\u672c\u5973\u4f18\u6749\u539f\u674f\u7483\u6700\u7f8e\u5199\u771f\u301013P\u3011.rar<\/dd>\n\t\n\t<dt>\u5927\u5c0f\uff1a<\/dt>\n\t<dd>2.03M<\/dd>\n\t\n\t<dt>\u4e0b\u8f7d\u6b21\u6570\uff1a<\/dt>\n\t<dd>1132 \u6b21<\/dd>\n\t\n\t<dt>\u6700\u540e\u66f4\u65b0\u65f6\u95f4\uff1a<\/dt>\n\t<dd>2018-8-4<\/dd>\n\t\n\t<dt>\u552e\u4ef7\uff1a<\/dt>\n\t<dd><span class=\"red\">0 \u91d1\u5e01<\/span><\/dd>\n\t\n\t<dt>\u60a8\u8d26\u6237\u5269\u4f59\uff1a<\/dt>\n\t<dd>0 \u91d1\u5e01<\/dd>\n\t\n\t<dt>\u4e0b\u8f7d\u5730\u5740\uff1a<\/dt>\n\t<dd><a href=\"http:\/\/www.1btjia.com\/attach-download-fid-8-aid-73175.htm\" target=\"_blank\"><span class=\"icon icon-download\"><\/span> <u><b>\u672c\u5730\u4e0b\u8f7d<\/b><\/u><\/a><\/dd>\n\t\n\t<dt><\/dt>\n\t<dd>\n\t\t<br \/>\n\t\t<!--<a type=\"submit\" class=\"button bigblue\" onclick=\"window.open('http:\/\/www.1btjia.com\/attach-download-fid-8-aid-73175.htm');;return false;\" id=\"down_click_73175\" value=\"\u70b9\u51fb\u4e0b\u8f7d\" href=\"javascript:void(0)\" role=\"button\"><span>\u70b9\u51fb\u4e0b\u8f7d<\/span><\/a>-->\n\t\t<a type=\"button\" class=\"button biggrey\" value=\"\u5173\u95ed\" id=\"down_cancel_73175\" href=\"javascript:void(0)\" role=\"button\"><span>\u5173\u95ed<\/span><\/a>\n\t<\/dd>\n<\/dl>\n\n<script type=\"text\/javascript\">\n\n\/\/ \u5ef6\u8fdf\u6267\u884c\u7684\u811a\u672c\uff0c\u7ea6\u5b9a\u540d\u5b57\u4e3a\uff1adelay_execute()\nfunction delay_execute(dialog, recall) {\n\t$('#down_cancel_73175').click(function() {\n\t\tdialog.close();\n\t});\n\t$('#down_click_73175').click(function() {\n\t\tdialog.close();\n\t});\n}\n<\/script>\n"}}

c = json.loads(c)
# print(c)
# print(a)
# pprint(c)
# print(c['message']['body'])
content=c['message']['body']
# content.replace('\\','')
doc = soup(content, 'html5lib')
# print(doc)
a = doc.find(class_=['icon-download']).parent
urlDown = a['href']
print(urlDown)
# wget.download(urlDown, out="./a.rar") 太慢了
# trList = soup(item, "html5lib")
# res = trList.find_all("th")
# print(res)

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100

    print ('\r' + '[下载进度]%s%.2f%%'%('>'*int(per),per),end='')


import urllib.request
# url = 'http://download.redis.io/releases/redis-5.0.5.tar.gz'

urllib.request.urlretrieve(urlDown, "demo.zip",Schedule)
