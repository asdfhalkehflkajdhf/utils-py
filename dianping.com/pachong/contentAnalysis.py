from bs4 import BeautifulSoup as soup

class contentAnalysis():
    def __init__(self, text):
        import chardet
        # res = chardet.detect(text)
        # text.encoding = res['encoding']
        self.doc = soup(text, 'html5lib')
        # 去除script
        # [s.extract() for s in self.doc('script')]

    def getBusinessHead(self):
        """
        # 第一个page
        :return:
        """

        '''获取标题'''
        basicInfo = self.doc.select('div[id=basic-info] h1')
        tdoc = soup('%s'%basicInfo[0], 'lxml')
        [a.extract() for a in basicInfo[0]('a')]
        h1 = tdoc.body.contents[0]

        '''获取评论'''
        basicInfo = self.doc.select('div[class=brief-info] ')
        bi = basicInfo[0]
        # print(bi)

        '''获取地址'''
        basicInfo = self.doc.select('div[class="expand-info address"] ')
        eia = basicInfo[0]
        # print(eia)

        '''获取电话'''
        basicInfo = self.doc.select('p[class="expand-info tel"] ')
        eit = basicInfo[0]
        # print(eit)

        return h1+bi+eia+eit

        # aTag = tdoc.select('a')
        # print(h1)
        # brief = tdoc.select('div[class=brief-info]')
        # phone = tdoc.select('p[class=brief-info]')
        #
        # print(basicInfo)
        # print(h1, brief, phone)

    def getLayoutList(self):
        """
        获取布局css　link
        :return:
        """
        links = self.doc.select('link[rel=stylesheet]')
        return [str(item).replace('href="//', 'href="http://') for item in links]

    def getReviewNumDict(self):
        """
        获取评论数,这个是在page页面获取的，点评
        :return:
        """
        rn = self.doc.select('div[class=tabs] em')
        if rn is None or rn.__len__()!=2:
            return [0,0]
        rn=[int(e.text.strip('() ')) for e in rn]
        return rn


    def getReviewsMaxPages(self):
        """
        获取评论最大页，用于fan页 ,注意没有评论时或是小于１页时　返回０
        :return:
        """
        try:
            rmp = self.doc.select('div[class=reviews-pages] a')
            if rmp is None:
                return 0
            return rmp[-2].text
        except Exception as e:
            return 0

    def getCommentLists(self):
        """
        返回[li标签评论内容]，[评论时间],[level]
        :return:
        """
        '''去删除所有的更多评论链接'''
        [a.extract() for a in self.doc.find_all('div', {'class': 'more-related-reviews'})]

        '''获取用户头像信息'''
        userPhotoList = self.doc.select('div[class=reviews-items] a[class=dper-photo-aside]')
        for a in userPhotoList:
            a['target']=''
            a['href']='jacascript::void(0);'
        # 转换头像
        userPhotoList=[str(a).replace('data-lazyload', 'src')  for a in userPhotoList]

        '''获取用户评论信息'''
        userCommentList = self.doc.select('div[class=reviews-items] div[class=main-review]')
        for a in userCommentList:
            for atag in a.select('a'):
                atag['target']=""
                atag['href'] = 'jacascript::void(0);'
        userCommentList=[str(a).replace('data-lazyload', 'src')  for a in userCommentList]

        '''获取用户评论时间信息'''
        userCommentDateList = self.doc.select('div[class=reviews-items] span[class=time]')
        userCommentDateList = [stime.text.strip() for stime in userCommentDateList]

        '''获取用户评论级别'''
        userCommentLevelList = self.doc.select('div[class=reviews-items] span[class*=sml-rank-stars]')
        userCommentLevelList = [int(level['class'][1][-2:]) for level in userCommentLevelList]
        # print(userCommentLevelList)

        return [ai+bi for ai,bi in zip(userPhotoList,userCommentList) ],userCommentDateList,userCommentLevelList

if __name__=="__main__":
    # tt = '<script>a</script>Hello World!<script>b</script>'
    # tsoup = soup("%s"%tt, 'lxml')
    # [s.extract() for s in tsoup('script')]
    # print(tsoup)

    with open('tttt.html', 'r', encoding='utf8') as f:
        t = contentAnalysis(f.read())
        t.getCommentLists()