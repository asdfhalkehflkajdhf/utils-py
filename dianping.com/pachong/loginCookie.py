import time
import logging

import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# 设置日志等级
logging.basicConfig(level=logging.INFO)


class SimulationOperation():
    def __del__(self):
        if self.browser:
            self.browser.close()
    def close(self):
        if self.browser:
            self.browser.close()

    def __init__(self):
        # 实例化谷歌设置选项
        options = webdriver.ChromeOptions()

        self.cookiePath = os.environ['LOCALAPPDATA'] + r"/Google/Chrome/User Data/Default/Cookies"
        self.userDataPath = os.environ['LOCALAPPDATA'] + r"/Google/Chrome/User Data"
        options.add_argument(r"user-data-dir=" + self.userDataPath)

        self.browser=None
        # 打开浏览器
        try:
            self.browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
        except Exception as e:
            logging.info("多个浏览器同时长开")

            exit(2)
        logging.info("inti ok")
        self.href = 'http://www.dianping.com/'

    def loginCookie(self, href=None):
        if href is None:
            href = self.href
        self.browser.get(href)
        time.sleep(2)
        # 检查是否登录成功
        isLogin=False
        try:
            loginName=self.browser.find_element_by_class_name('username').text
            print('登录成功：'+loginName)
            isLogin=True
        except Exception as e:
            # 没有登录成功，生成登录警告信息,写入相应日志文件，从web服务直接重新启动
            logMsg="需要进行登录，并设置为自动感登录状态"
            logging.log(logMsg)
            isLogin=False

        return isLogin

    def toPage(self, url, openNum=2):
        """
        返回页面代码,等待解析
        :param url:
        :return:
        """
        # 新开一个窗口，通过执行js来新开一个窗口
        js = 'window.open("%s");'%url
        self.browser.execute_script(js)
        # 添加最后一次打开的页面
        handles = self.browser.window_handles
        if handles > openNum:
            # 关闭当前
            self.browser.close()
        # 跳转到新页面
        self.browser.switch_to.window(handles[-1])
        return self.browser.page_source
        pass

    def saveTextTo(self,path):
        with open(path, 'w', encoding='utf8') as f:
            print(self.browser.page_source, file=f)








if __name__=="__main__":
    t = SimulationOperation()
    t.loginCookie()

