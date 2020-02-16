import datetime
import re
import requests
from bs4 import BeautifulSoup as soup
from pprint import pprint
import xml.etree.ElementTree as et
import time


gNowDate = datetime.datetime.now()
# now = datetime.datetime.now() + datetime.timedelta(days=-1)
gUrlRoot = "http://www.newsmth.net"
'''
水木，内容请求
'''
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

def collect_article_links(pageNum, endPage, filename='links.txt',
                          url='http://www.1btjia.com/forum-index-fid-8-page-%d.htm'):
    '''
    收集网站的文章链接
    '''

    if pageNum > endPage:
        return
    """
    第一步，请求数据
    """
    url = url%(pageNum)
    res = []
    content = extract_content(url)
    if content.__len__()==0:
        return

    doc = soup(content, 'html5lib')
    # 获取当前页的所有记录 thread-old thread-digest-1 thread-new
    # 解决办法：soup.find(class_=['abc', 'def'])
    # aList = doc.find_all(class_ ="subject_link")[1:]
    aList= doc.find_all(class_ =['thread-old', 'thread-digest-1', 'thread-new'])[0:]
    # print(aList)

    for idx in range(aList.__len__()):
        #  对记录时行解析
        a = aList[idx]
        # print(a)
        res.append(a['href'].split('-')[-1]+a.get_text()+'\n'+ a['href'] + "\n" )

    print("page [%d] 获取记录 [%d]"%(pageNum, res.__len__()))
    # 有数据写入文件
    if res.__len__():
        fout = open(filename, 'at', encoding='utf-8')
        fout.writelines(res)
        fout.close()


        # 下一页内容
    collect_article_links(pageNum+1, endPage, filename)

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

    now = datetime.datetime.now()+datetime.timedelta(days=-30)
    parser.add_option('-e', '--end-page', dest='endPage', help='默认为 all',default="all")
    parser.add_option('-f', '--link-file', dest='linkFile', help='默认 links-YYYY-MM-DD.txt', default="getPageList-"+gNowDate.date().__str__()+".txt")
    parser.add_option('-p', '--start-page', dest='pageNum', help='默认为1', default=1)
    (options, args) = parser.parse_args()
    print(options)


    if options.endPage == "all":
        options.endPage = 10
    # options.endPage = datetime.datetime.strptime("2009-01-01", "%Y-%m-%d")

    collect_article_links(pageNum=options.pageNum, endPage=options.endPage, filename=options.linkFile)




    print("end")