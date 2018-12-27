import os
import time

from PIL import Image
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

'''https://blog.csdn.net/xiongzaiabc/article/details/82912280'''

def get_snap(driver):  # 对目标网页进行截屏。这里截的是全屏
    driver.save_screenshot('full_snap.png')
    page_snap_obj = Image.open('full_snap.png')
    return page_snap_obj
def del_snap():
    if os.path.isfile('full_snap.png'):
        os.remove('full_snap.png')

def get_image(location, screenImg):  # 对验证码所在位置进行定位，然后截取验证码图片
    image_obj = screenImg.crop((location['left'], location['top'], location['right'], location['bottom']))
    # image_obj.show()
    return image_obj  # 得


if __name__=="__main__":
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    time.sleep(3)

    screenImg = get_snap(browser)
    time.sleep(2)
    # 获取图片对象
    img = browser.find_element_by_tag_name('img')

    # 保存图片
    location = {}
    location['left']=img.location['x']
    location['top'] = img.location['y']
    location['right']=location['left']+img.size['width']
    location['bottom'] = location['top']+img.size['height']

    image_obj = get_image(location, screenImg)
    image_obj.save("baidu.png")

    # 删除临时文件
    del_snap()