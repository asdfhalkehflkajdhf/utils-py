import datetime
import json
import re

import os
import requests
from bs4 import BeautifulSoup as soup
from pprint import pprint
import xml.etree.ElementTree as et
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

gNowDate = datetime.datetime.now()
gUrlRoot = "http://www.pximg.com/meinv"
'''
内容请求
'''
def extract_content(url):
    '''
    抽取南方周末的报道列表
    '''
    try:
        response = requests.get(url)
        response.encoding="utf-8"
    except Exception as e:
        print("Exception: {}".format(e))
        print(url)
        return ""
    else:
        time.sleep(6)
        return response.text

def schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100

    print ('\r' + '[下载进度]%s%.2f%%'%('>'*int(per/2),per),end='')
def download_img(img_url, out_fname):
    try:
        r = requests.get(img_url, stream=True, timeout=60)
    except requests.exceptions.RequestException as e:
        print(e, img_url, out_fname)
        return
    # print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open(out_fname, 'wb').write(r.content) # 将内容写入图片
    else:
        print(r.status_code , img_url, out_fname)
    del r

def collect_article_links(listPara):
    '''
    收集网站的文章链接
    '''
    putPath, dirName, url, idx=listPara
    def collect_article_links_branch(savePath, url):
        """
        第一步，请求数据
        """
        res = []

        content = extract_content(url)
        if content.__len__() == 0:
            print("error ", dirName, url)
            return
        # 获取数据解出图片地址
        doc = soup(content, 'html5lib')
        divlist = doc.find('ul', class_=['gallery_demo_unstyled'])
        imgList = divlist.find_all("img")
        # print(imgList)

        for img in imgList:
            result = urllib.parse.urlsplit(img['src'])
            dataUrl = dict(urllib.parse.parse_qsl(result.query))['src']
            out_fname = os.path.join(savePath, "_".join(dataUrl.split('/')[-3:]))
            # print(dataUrl, out_fname)
            download_img(dataUrl, out_fname)
            
        


    savePath = os.path.join(putPath, dirName)
    if dirName:
        if os.path.exists(savePath):
            # 目录存在则直接退出
            print("行号", idx, "目录已存在 ", dirName)
            return
        os.mkdir(savePath)
    # 非空 就 打开链接
    if url:
        collect_article_links_branch(savePath, url)
        None
    print("行号", idx, "完成下载 ", dirName)


"""这个使用浏览器使用账号登陆，就可以执行"""
if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-f', '--link-file', dest='linkFile', help='默认 getPageList.txt', default="getPageList.txt")
    parser.add_option('-p', '--put-path', dest='putPath', help='默认为当前目录', default="./")
    (options, args) = parser.parse_args()
    print(options)

    options.putPath = u"F://个人 - meitu/www.pximg.com.meinv"


    with open(options.linkFile, "r", encoding='utf8') as alink:
        lines = alink.readlines()
        mapPara = [[options.putPath,lines[idx].rstrip() , lines[idx+1].rstrip(), idx] for idx in range(0,lines.__len__(),2)]

    with ThreadPoolExecutor(12) as actuator:
        actuator.map(collect_article_links, mapPara)


    print("end")