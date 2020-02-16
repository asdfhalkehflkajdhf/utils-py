import os

import requests
from bs4 import BeautifulSoup as soup
import re
# import sqlite3

import time

from concurrent.futures import ThreadPoolExecutor

# gconn = sqlite3.connect('7160.db')
gUrlRoot = "http://www.7160.com"
gSaveRootDir=u"F://个人 - meitu/www.7160.com"
gLogFile = open('runlog.txt','a')
gPageFile = open('downpagelog.txt','a')

gSubThreadNum=1
gPageThreadNum=10
gDownImgThreadNum=10

# 14风景 15美食
glevelDict = {
    'rentiyishu': {'http': 'https', 'cname': '人体艺术', 'listid':'1', 'startPage':110, 'endPage':-1, 'downSub':False}
    ,'qingchunmeinv': {'http': 'http', 'cname': '清纯美女', 'listid':'2', 'startPage':267, 'endPage':-1, 'downSub':False}
          	,'xingganmeinv': {'http': 'http', 'cname': '性感美女', 'listid':'3', 'startPage':327, 'endPage':-1, 'downSub':False}
          	,'xingganmote': {'http': 'http', 'cname': '性感模特', 'listid':'4', 'startPage':256, 'endPage':-1, 'downSub':False}
          	,'meinvmingxing': {'http': 'http', 'cname': '美女明星', 'listid':'5', 'startPage':62, 'endPage':-1, 'downSub':False}
          	,'xiaohua': {'http': 'https', 'cname': '校园美女', 'listid':'6', 'startPage':1, 'endPage':-1, 'downSub':True}
            ,'yulebagua': {'http': 'https', 'cname': '娱乐八卦', 'listid':'7', 'startPage':1, 'endPage':-1, 'downSub':False}
          	,'lianglichemo': {'http': 'http', 'cname': '靓丽车模', 'listid':'8', 'startPage':1, 'endPage':-1, 'downSub':True}
			,'Cosplay': {'http': 'https', 'cname': 'cosplay', 'listid':'9', 'startPage':1, 'endPage':-1, 'downSub':False}
          	,'rihanmeinv': {'http': 'http', 'cname': '日韩美女', 'listid':'10', 'startPage':1, 'endPage':-1, 'downSub':False}
          	,'zhenrenxiu': {'http': 'http', 'cname': '真人秀', 'listid':'11', 'startPage':1, 'endPage':-1, 'downSub':False}
			,'oumeimeinv': {'http': 'http', 'cname': '欧美美女', 'listid':'12', 'startPage':1, 'endPage':-1, 'downSub':False}
          	,'weimeitupian': {'http': 'http', 'cname': '唯美图片', 'listid':'13', 'startPage':1, 'endPage':-1, 'downSub':False}
              }

def checkDir(news_title):
    char_list = ['*', '|', ':', '?', '/', '<', '>', '"', '\\']
    for i in char_list:
        if i in news_title:
            news_title = news_title.replace(i, "_")
    return news_title

def getNumForStr(s):
    s1 = re.findall(r"\d+\.?\d*", s)
    if s1.__len__()<1:
        return 0
    return int(s1[0])

def extract_content(url):
    '''
    请求内容
    '''
    try:
        r = requests.get(url)
        r.encoding="gbk"
        return r.text
    except Exception as e:
        print("openError", url, "Exception: {}".format(e),file=gLogFile,flush=True)
        return ""
    # else:
        # time.sleep(6)
def save_to_mongo(img_url, title, talbe):
    try:
        sql = "INSERT INTO %s (title,url) VALUES ('%s', '%s')"%(talbe,title,img_url)
        # gconn.execute(sql)
    except Exception:
        None
def save_to_dir(img_url, out_fname):
    again=False
    try:
        r = requests.get(img_url, stream=True, timeout=120)
        if r.status_code == 200:
            open(out_fname, 'wb').write(r.content)  # 将内容写入图片
        else:
            # print('downError','{"url":"%s","path":"%s"}'%(img_url, out_fname),"Exception: {}".format(r.status_code),file=gLogFile,flush=True)
            pass
    except requests.exceptions.RequestException as e:
        again=True
    except Exception as e:
        print('downError', '{"url":"%s","path":"%s"}' % (img_url, out_fname), "Exception: {}".format(r.status_code),
              file=gLogFile, flush=True)
    if not again:
        return

    # 再次一次
    time.sleep(10)
    try:
        r = requests.get(img_url, stream=True, timeout=120)
        if r.status_code == 200:
            open(out_fname, 'wb').write(r.content)  # 将内容写入图片
        else:
            # print('downError','{"url":"%s","path":"%s"}'%(img_url, out_fname),"Exception: {}".format(r.status_code),file=gLogFile,flush=True)
            pass
    except requests.exceptions.RequestException as e:
        print('downError', '{"url":"%s","path":"%s"}' % (img_url, out_fname), "Exception: {}".format(e),
              file=gLogFile, flush=True)
        return

    # del r

def download_img(para):
    Son_link, l, v = para
    rootHttp = v['http'] + '://www.7160.com'
    if v['listid']=='6' or v['listid']=='8':
        Sonson_link=rootHttp+Son_link[:-5] + "_%d"%l + Son_link[-5:]
    else:
        Sonson_link=rootHttp+Son_link+'index_'+str(l)+'.html'
    # print( Sonson_link)
    content = extract_content(Sonson_link)
    if content.__len__() == 0:
        return
    # 获取数据解出图片地址
    doc = soup(content, 'html5lib')
    image_son = doc.select('.picsbox  p a img')[0]
    src = image_son['src']
    alt = image_son['alt']

    savePath = os.path.join(v['savedir'], src.split('/')[-1])
    if os.path.exists(savePath):
        # 文件存在
        return

    save_to_mongo(src, v['title'],v['table'])
    save_to_dir(src, savePath)
# 按页进行子主题下载
def subject_link(para):
    subTitle,v,pageId=para

    url=v['http']+'://www.7160.com/'+subTitle+'/list_'+v['listid']+'_'+str(pageId)+'.html'
    print('开始下载 %s 主题,第 %d 页'%(subTitle,pageId),file=gPageFile,flush=True)

    content = extract_content(url)
    if content.__len__() == 0:
        return pageId
    # 获取数据解出图片地址
    doc = soup(content, 'html5lib')
    items=doc.select('.news_bom-left li > a')
    for item in items:
        # 打开主题第一页
        Son_link=item['href']
        rootHttp = v['http'] + '://www.7160.com'
        url=rootHttp+Son_link
        son_content = extract_content(url)
        doc2 = soup(son_content, 'html5lib')
        try:
            image_main = doc2.select('.picsbox  p a img')[0]
        except IndexError:
            print('openError', url,file=gLogFile,flush=True)
            continue
        src=image_main['src']
        alt=checkDir(image_main['alt'])
        saveDir=src.split('/')[-2]+'_'+alt
        saveDir = os.path.join(gSaveRootDir,v['cname'],saveDir)

        nv={}
        nv['table']=subTitle
        nv['listid']=v['listid']
        nv['http']=v['http']
        nv['savedir']=saveDir
        nv['title']=alt
        # 新建主题目录
        if not os.path.exists(saveDir):
            os.makedirs(saveDir)
        savePath = os.path.join(saveDir, src.split('/')[-1])
        save_to_mongo(src, alt,subTitle)
        save_to_dir(src,savePath)
        #获取页码
        try:
            pageTag=doc2.select('.itempage a:nth-of-type(1)')[0].text
        except IndexError:
            print('openError', url,file=gLogFile,flush=True)
            return
        page_num=getNumForStr(pageTag)+1

        # 从第二页开始进行重复爬取数据，同时进行爬
        mapPara = [(Son_link, i, nv) for i in range(2, page_num)]
        with ThreadPoolExecutor(gDownImgThreadNum) as actuator:
            actuator.map(download_img, mapPara)

    return pageId
# 每一个主题起一个多线程
def subject_page(para):

    k,v=para
    if not v['downSub']:
        return
    #检查目录
    checkSaveDir(k,v)
    # 获取最大页数
    url = '/'.join([gUrlRoot,k,''])
    content = extract_content(url)
    if content.__len__() == 0:
        return
    doc = soup(content, 'html5lib')
    try:
        subPageNum = getNumForStr(doc.select('.ne-to-right h6')[0].text)//28+1
        print(k,getNumForStr(doc.select('.ne-to-right h6')[0].text))
    except IndexError:
        print('openError', url,file=gLogFile,flush=True)
        return
    if v['endPage']!=-1 and subPageNum>v['endPage']:
        subPageNum=v['endPage']

    mapPara = [(k,v,i) for i in range(v['startPage'],subPageNum)]
    with ThreadPoolExecutor(gPageThreadNum) as actuator:
        for result in actuator.map(subject_link, mapPara):
            pass
#检查子目录
def checkSaveDir(key,subt):
    '''
    :return:
    '''
   #  gconn.execute('''CREATE TABLE IF NOT EXISTS %s
   # (id INTEGER PRIMARY KEY NOT NULL,
   # title      CHAR(256),
   # url        CHAR(256));'''%key)
    saveDir = os.path.join(gSaveRootDir, subt['cname'])
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
def main():

    mapPara = [[key, subt] for key, subt in glevelDict.items()]
    with ThreadPoolExecutor(gSubThreadNum) as actuator:
        for result in actuator.map(subject_page, mapPara):
            pass

if __name__ == '__main__':
    main()