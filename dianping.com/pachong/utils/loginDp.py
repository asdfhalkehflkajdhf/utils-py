# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:57:22 2018

@author: wmq
"""

import logging
import time

import getCodeImg_JieTu
from selenium import webdriver

# 设置用户名密码
username_ = ""
password_ = ""

# 设置日志等级
logging.basicConfig(level=logging.INFO)

# 打开浏览器
browser = webdriver.Chrome("chromedriver.exe")
href = 'http://www.dianping.com/'
browser.get(href)
time.sleep(2)

# 选择登录
try:
    login_btn = browser.find_element_by_class_name('login-container').find_element_by_partial_link_text('登录').click()
    time.sleep(3)
except Exception as e:
    print(e.args)
    exit(1)

# 打开登录页面
try:
    iframe =  browser.find_element_by_tag_name('iframe')
    browser.switch_to.frame(iframe)   # 切换至登录模块iframe
except Exception as e:
    print(e.args)
    exit(1)

# 选择PC登录
try:
    icon_pc = browser.find_element_by_class_name('icon-pc').click()
    time.sleep(2)
except Exception as e:
    print(e.args)
    exit(1)

# 选择密码登录
try:
    name_login = browser.find_element_by_xpath('//*[@id="tab-account"]')
    name_login.click()
    time.sleep(2)
except Exception as e:
    print(e.args)
    exit(1)

# 输入用户名,密码
try:
    username = browser.find_element_by_xpath('//input[@id="account-textbox"]')
    password = browser.find_element_by_xpath('//input[@id="password-textbox"]')
    username.clear()
    username.send_keys(username_)
    password.clear()
    password.send_keys(password_)
except Exception as e:
    print(e.args)
    exit(1)

# 提交登陆
try:
    sub_btn = browser.find_element_by_xpath('//button[@id="login-button-account"]')
    sub_btn.click()
    time.sleep(2)
except Exception as e:
    print(e.args)
    exit(1)

# 获取登录信息
alertTimes=3
while True:
    alert = browser.find_element_by_id('alert').text
    if alert is not None:
        if alert=='为保证您的账户安全，请用短信验证登录':
            alertTimes=alertTimes-1
            sub_btn = browser.find_element_by_xpath('//button[@id="login-button-account"]')
            sub_btn.click()
            time.sleep(2)
        elif alert=='请输入图形验证码':
            break
    else:
        time.sleep(1)

    if alertTimes<1:
        exit(2)



# 获取验证吗图片并解析
code_img_path = "captcha.png"

code_img = browser.find_element_by_xpath('//*[@id="captcha-account-container"]').find_element_by_tag_name('img')
screenImg = getCodeImg_JieTu.get_snap(browser)

# 保存图片
location = {}
location['left'] = code_img.location['x'] + iframe.location['x']
location['top'] = code_img.location['y'] + iframe.location['y']
location['right'] = location['left'] + code_img.size['width']+ iframe.location['x']
location['bottom'] = location['top'] + code_img.size['height']+ iframe.location['y']


code_img_obj = getCodeImg_JieTu.get_image(location, screenImg)
code_img_obj.save(code_img_path)
assert False
code_value = getVerificationCode.getCodeTextValue(code_img_path)
print(code_value)

# 输入验证码
verify_code = browser.find_element_by_xpath('//*[@id="captcha-textbox-account"]')
verify_code.clear()
verify_code.send_keys(code_value)

# 提交登陆
sub_btn = browser.find_element_by_xpath('//*[@id="login-button-account"]')
sub_btn.click()
time.sleep(5)

alertTimes=3
while True:
    alert = browser.find_element_by_id('alert').text
    if alert is not None:
        if alert=='验证码错误':
            alertTimes=alertTimes-1
            sub_btn = browser.find_element_by_xpath('//button[@id="login-button-account"]')
            sub_btn.click()
            time.sleep(2)
        elif alert=='请输入图形验证码':
            break
    else:
        time.sleep(1)

    if alertTimes<1:
        exit(2)



# 切换回主页
browser.switch_to.default_content()
