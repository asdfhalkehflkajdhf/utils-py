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

def download_img(para):
    img_url, out_fname = para
    try:
        r = requests.get(img_url, stream=True, timeout=120)
    except requests.exceptions.RequestException as e:
        print(e, img_url, out_fname)
        return
    # print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open(out_fname, 'wb').write(r.content) # 将内容写入图片
    print(r.status_code , img_url, out_fname)
    del r


def chouquData():
    '''
    从结果数据中获取数据
    :return:
    '''
    resh=[]
    rese=[]
    linkFile = 'new.txt'
    with open(linkFile, "r", encoding='utf8') as f:
        for lines in f.readlines():
            if not lines.startswith('404'):
                if lines.startswith('行号') and '目录已存在' in lines:
                    resh.append(lines)
                elif not lines.startswith('行号') and not lines.strip().endswith('rar') :
                    rese.append(lines)
    fout = open('error.txt', 'w', encoding='utf-8')
    fout.writelines(rese)
    fout.writelines(resh)
    fout.close()

def reDownLoad():

    putPath = u"F://个人 - meitu/www.1btjia.com"

    linkFile = 'error.txt'
    with open(linkFile, "r", encoding='utf8') as alink:
        lines = alink.readlines()
        mapPara = [[lines[idx].rstrip(), lines[idx + 1].rstrip()] for idx in range(0, lines.__len__(), 2)]


    with ThreadPoolExecutor(12) as actuator:
        actuator.map(download_img, mapPara)

    print("end")
"""这个使用重试出错行"""
if __name__ == '__main__':
    # chouquData()
    reDownLoad()