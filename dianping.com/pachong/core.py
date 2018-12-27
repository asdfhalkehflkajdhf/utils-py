''''''
'''核心功能
向服务器发送验证请求获得结果

发送的信息：
硬盘序列号：
当前时间：

id:服务器返回的一个自增ID
code: [0,1,2,3,4]
msg:[
ok,
服务时间结束，联系方式
未注册，联系方式
网络链接超时，联系方式
用户未接入网络，联系方式
]
'''


'''重新启动'''

'''参数
商户ID list
时间间隔
'''

'''程序有两个部分
启动心跳在线测试,ping一个服务器，更新本地db时间
时间间隔爬取商户逻辑,数据写入本地数据库
'''

import  deviceInfo
import linkServer
import optparse



def reptilePage(options):
    # 获取硬盘序列号
    HDSerialNumber = deviceInfo.get_disk_info()
    # 获取登录信息
    loginDict = linkServer.linkServer("localhost", "root", "123456", "dianpingstatusvalidation").getLinkState(HDSerialNumber)
    if loginDict is not None and loginDict['code']!=0:
        '''写入页面,结束程序'''
        exit(loginDict['code'])

    # 获取登录成功,启动程序

    pass

def sendHeartBeat():
    # 获取硬盘序列号
    HDSerialNumber = deviceInfo.get_disk_info()
    loginDict = linkServer.linkServer("localhost", "root", "123456", "dianpingstatusvalidation").setHeartBeat(HDSerialNumber)
    if loginDict is not None and loginDict['code']!=0:
        '''写入页面,结束程序'''
        pass
    else:
        pass

"""==============================================="""
_OPT = optparse.OptionParser()
_OPT.add_option('-c', '--heartbeat', action="store_true", dest="heartBeat", default=False, help='发送心跳')

# _OPT.add_option('-d', '--dataDir', action='store', dest='dataDir', default="res/trainRes-2018-11-12 aitken/*", help='数据目录(这个是主题数据目录，不是原始数据): default="res/trainRes/*"')
# _OPT.add_option('--resRootDir', action='store', dest='resRootDir', default="res", help='echars json结果存放数据目录: default="res"')
# _OPT.add_option('--resFileName', action='store', dest='resFileName', default="sample", help='结果存放数据目录: default="sample"')
# _OPT.add_option('--startDate', action='store', dest='startDate', help='开始日期: 格式YYYY-MM-DD')
# _OPT.add_option('--level', action='store', dest='level', help='显示层次')
# _OPT.add_option('--symbolSize', action='store', dest='symbolSize', type='int', default=20, help='显示大小归一化:default=20')
# _OPT.add_option('--linkSize', action='store', dest='linkSize', type='float', default=2.5, help='过滤小于２的边:default=2')
# _OPT.add_option('--heatFilter', action='store', dest='heatFilter', type='float', default=300, help='过滤热度小于100的点:default=300')
# _OPT.add_option('--topK', action='store', dest='topK', type='int', default=5, help='每天前Ｎ个最大的热点:default=5')

# _OPT.print_help()
"""==============================================="""

if __name__=="__main__":
    options, _ = _OPT.parse_args()


    if options.heartBeat:
        sendHeartBeat()
    else:
        reptilePage(options)




