import datetime
import json
import re

import os
import requests
from bs4 import BeautifulSoup as soup
from pprint import pprint
import xml.etree.ElementTree as et
import time

import urllib.request
from concurrent.futures import ThreadPoolExecutor


gUrlRoot = "http://www.1btjia.com"
'''
内容请求
'''
def extract_content(url):
    '''
    抽取南方周末的报道列表
    '''
    try:
        response = requests.get(url,headers = { 'Connection': 'close'})
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
        r = requests.get(img_url, stream=True, timeout=120)
    except requests.exceptions.RequestException as e:
        print("DOWN", img_url, out_fname)
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
        content = extract_content(url)
        if content.__len__() == 0:
            print("error ", dirName, url)
            return False

        doc = soup(content, 'html5lib')
        # 获取当前页的所有记录 thread-old thread-digest-1 thread-new
        # 解决办法：soup.find(class_=['abc', 'def'])
        # aList = doc.find_all(class_ ="subject_link")[1:]

        # 判断有没有附件
        attachlist = doc.find_all(class_=['attachlist'])
        # print(attachlist)
        if attachlist:
            #     有附件
            ajaxdialog = attachlist[0].find_all(class_=['ajaxdialog'])[0]
            # print(ajaxdialog)
            dataUrl = ajaxdialog['href']
            # 请求下载地址
            resJson = extract_content(dataUrl)
            resJson = json.loads(resJson)

            downlaodContent = resJson['message']['body']
            downlaodDoc = soup(downlaodContent, 'html5lib')
            downlaodA = downlaodDoc.find(class_=['icon-download']).parent
            downlaodUrl = downlaodA['href']
            out_fname = os.path.join(savePath, ajaxdialog.get_text())

                # urllib.request.urlretrieve(dataUrl, out_fname, schedule)
                # urllib.request.urlretrieve(dataUrl, out_fname)
            download_img(downlaodUrl, out_fname)

        else:

        # 没有附件
            imgDiv=doc.find_all(class_=['message'])[0]

            imgList = imgDiv.find_all("img")
            # print(imgList)
            for idx in range(imgList.__len__()):
                #  对记录时行解析
                dataUrl = imgList[idx]["src"]
                out_fname= os.path.join(savePath, os.path.basename(dataUrl))
                # urllib.request.urlretrieve(dataUrl, out_fname, schedule)
                # urllib.request.urlretrieve(dataUrl, out_fname)
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


# def collect_articles(link_file, article_file='articles.xml'):
#     '''
#     读取保存文章链接的文件，访问每一个文章链接，构建文章数据集
#     '''
#     fin = open(link_file, 'r')
#     links = [a.strip() for a in fin.readlines()]
#     fin.close()
#     tree = et.ElementTree()
#     root = et.Element('articles')
#     tree._setroot(root)
#
#     count = 0
#     for url in links:
#         count += 1
#         print(count, '\t', url)
#         try:
#             title, content, tags = extract_content(url)
#             print(title)
#             if len(tags) < 3:
#                 continue
#             item = et.Element("article")
#             root.append(item)
#             et.SubElement(item, 'url').text = url
#             et.SubElement(item, 'title').text = title
#             et.SubElement(item, 'tags').text = ','.join(tags)
#             et.SubElement(item, 'content').text = content
#         except:
#             print('Error:', url, '...')
#
#     tree.write(article_file, 'utf-8')
#
#     print('finished.')

"""这个使用浏览器使用账号登陆，就可以执行"""
if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()

    parser.add_option('-f', '--link-file', dest='linkFile', help='默认 getPageList.txt', default="getPageList.txt")
    parser.add_option('-p', '--put-path', dest='putPath', help='默认为当前目录', default="./")
    (options, args) = parser.parse_args()
    print(options)

    options.putPath = u"F://个人 - meitu/www.1btjia.com"

    linkFile = 'getPageList.txt'
    with open(linkFile, "r", encoding='utf8') as alink:
        lines = alink.readlines()
        mapPara = [[options.putPath, lines[idx].rstrip(), lines[idx + 1].rstrip(), idx] for idx in range(0, lines.__len__(), 2)]

    with ThreadPoolExecutor(12) as actuator:
        actuator.map(collect_article_links, mapPara)

    print("end")