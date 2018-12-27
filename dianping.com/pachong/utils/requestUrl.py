import requests
import time
import utils.时间戳 as util
import utils.randomIntSleep as RISleep
# import log
# import g_config
import time
import random
from utils.user_agents import agents
import chardet

def getRequestHeaderDict():
    '''
    这个是自己电脑访问的
    Connection: keep-alive
Cache-Control: max-age=0
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: U_TRS1=00000037.699b22af.589bfe3d.574a9b13; vjuids=3ae24709.15a215a09c2.0.022725107205a; SINAGLOBAL=106.118.169.55_1486618177.295032; vjlast=1491299249.1491549143.11; SGUID=1492335099913_84642544; SCF=ArHFvsR3uUj2Qpjsgu-bK0sEBCyhvVwo87Yj9a9pmryeQQ1z5fpyLp0Bcu_5vR25jd7YE0yGA2qKR5kTJexe94Q.; sso_info=v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLaMk5ywjJOcs42TpLmJp5WpmYO0toyTnLCMk5yzjZOkuQ==; SUB=_2AkMuEaF0f8NxqwJRmP0VyGPjaI92yQDEieKYTVCvJRMyHRl-yD9kqnQttRB_fMYA61ZiKOM0vcsqgP6pqdSYLQ..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFm34fLmfUshS4Cd6GNU-NW; _ct_uid=59749e12.3a8810af; UOR=,,; ArtiFSize=14; lxlrtst=1518245252_o; ULV=1518250236498:56:5:5:183.198.27.226_1518250228.425347:1518250231445; UM_distinctid=1617fde5160116-06c5a853264da-3b3e5906-100200-1617fde5161122; lxlrttp=1518245252
    :return:
    '''
    '''qq必须添加头部'''
    agent = random.choice(agents)
    # 后继在评论会用到
    referer = "http://news.qq.com/"
    # 构建页面请求的头部
    headers = {'User-Agent': agent, "Referer": referer}
    # headers = {'User-Agent': agent}
    return headers
    pass

def requestUrl(url, timeout=20, headers=None,timesMax=3):
    times= 0
    while times<timesMax:
        try:
            if headers is None:
                headers={}

            # 设置不保存缓存  allow_redirects=False是不处理302
            headers['Cache-Control'] = 'no-cache'
            # time.sleep(RISleep.getRandomSleep(g_config.conf_Interval_time))
            print('开始请求----',end='')
            otherResponse = requests.get(url, headers=headers, timeout=timeout, allow_redirects=False)
            otherResponse.close()
            print('请求成功')
            res = chardet.detect(otherResponse.content)
            otherResponse.encoding=res['encoding']

            return otherResponse
        except requests.exceptions.ConnectTimeout:
            times+=1
            print(times," 请求超时,断开过一分钟　再试", url)
            time.sleep(60)
        except:
            print('请求失败')
            times+=1
            print(times," 请求超时,断开过一分钟　再试", url)
            time.sleep(60)
    pass #while times
    return None
pass #requestUrl

