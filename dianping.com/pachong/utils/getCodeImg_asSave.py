# 1、截屏，裁减
#     验证码位置选择
#       系统工具，元素位置　
# location = img.location
# left = location['x']
#     top = location['y']
#     right = left + size['width']
#     bottom = top + size['height']

#　2、右击另存为
#       另存为路径设置，和对话框处理，直接设置浏览器参数


# req = requests.get(url='https://verify.meituan.com/v2/captcha?request_code=45c4c73efcea42ed85a8f774f8e43bda&action=login',
#                     headers={'Date': 'Tue, 04 Dec 2018 14:22:15 GMT', 'M-TraceId':'659577734713269804'})  # buld post body data
# # 将获取到的图片二进制流写入本地文件
# with open('ttt.png', 'wb') as f:
#     # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
#     f.write(req.content)

from selenium import webdriver

import os
import requests
import time

from selenium import webdriver
# 1、截屏，裁减
#     验证码位置选择
#       系统工具，元素位置　
# location = img.location
# left = location['x']
#     top = location['y']
#     right = left + size['width']
#     bottom = top + size['height']

#　2、右击另存为
#       另存为路径设置，和对话框处理，直接设置浏览器参数


# req = requests.get(url='https://verify.meituan.com/v2/captcha?request_code=45c4c73efcea42ed85a8f774f8e43bda&action=login',
#                     headers={'Date': 'Tue, 04 Dec 2018 14:22:15 GMT', 'M-TraceId':'659577734713269804'})  # buld post body data
# # 将获取到的图片二进制流写入本地文件
# with open('ttt.png', 'wb') as f:
#     # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
#     f.write(req.content)

from PIL import Image

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'e:/login'}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

href = 'https://verify.meituan.com/v2/captcha?request_code=45c4c73efcea42ed85a8f774f8e43bda&action=login'
browser.get(href)
img =  browser.find_element_by_tag_name('img')
# browser.switch_to.active_element()

# 保存验证码
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

action = ActionChains(browser).move_to_element(img)#移动到该元素
action.context_click(img)#右键点击该元素

'''无法操作系统菜单，只能是页面内的'''
time.sleep(1)
action.key_down(Keys.SHIFT).send_keys('v').key_up(Keys.SHIFT).perform()#点击键盘向下箭头
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
# action.perform()#执行保存




