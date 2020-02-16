import datetime
import re
import requests
from bs4 import BeautifulSoup as soup
from pprint import pprint
import xml.etree.ElementTree as et
import time

gNowDate = datetime.datetime.now()
gUrlRoot = "https://www.pximg.com/meinv"
'''
内容请求
'''
def extract_content(url):
    '''
    抽取南方周末的报道列表
    '''
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        # print(response.text)
    except Exception as e:
        print("Exception: {}".format(e))
        print(url)
        return ""
    else:
        time.sleep(6)
        return response.text

def collect_article_links(pageNum, endPage, filename='links.txt',
                          url='https://www.pximg.com/meinv/page/%d'):
    '''
    收集网站的文章链接
    '''

    if pageNum > endPage:
        return
    """
    第一步，请求数据
    """
    if pageNum==1:
        url = gUrlRoot
    else:
        url = url%(pageNum)
    res = []
    content = extract_content(url)
    # print(content)
    if content.__len__()==0:
        return

    doc = soup(content, 'html5lib')
    # 获取当前页的所有记录 thread-old thread-digest-1 thread-new
    # 解决办法：soup.find(class_=['abc', 'def'])
    # aList = doc.find_all(class_ ="subject_link")[1:]
    ulList= doc.find(class_ =['camWholeBoxUl'])
    # print(ulList)
    aList = ulList.find_all("a", class_='itemimg')
    
    for idx in range(aList.__len__()):
        #  对记录时行解析
        a = aList[idx]
        # print(a)
        
        res.append( a['href'].split('/')[-1]+"_"+a['title']+'\n'+ a['href'] + "\n" )

    print("page [%d] 获取记录 [%d]"%(pageNum, res.__len__()))
    # 有数据写入文件
    if res.__len__():
        fout = open(filename, 'at', encoding='utf-8')
        fout.writelines(res)
        fout.close()


        # 下一页内容
    collect_article_links(pageNum+1, endPage, filename)


"""这个使用浏览器使用账号登陆，就可以执行"""
if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()

    now = datetime.datetime.now()+datetime.timedelta(days=-30)
    parser.add_option('-e', '--end-page', dest='endPage', help='默认为 all 25page',default="all")
    parser.add_option('-f', '--link-file', dest='linkFile', help='默认 links-YYYY-MM-DD.txt', default="getPageList-"+gNowDate.date().__str__()+".txt")
    parser.add_option('-p', '--start-page', dest='pageNum', help='默认为1', default=1)
    (options, args) = parser.parse_args()
    print(options)


    if options.endPage == "all":
        options.endPage = 44
    # 到2020年2月12号，也就44页

    collect_article_links(pageNum=options.pageNum, endPage=options.endPage, filename=options.linkFile)

    print("end")