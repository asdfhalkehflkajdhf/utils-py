from time import sleep
import telnetlib
import datetime
import sys
from optparse import OptionParser


sleeptime=3
glog=sys.stdout
debugLevel=0


def do_telnet(Host, username, password):
    '''''Telnet远程登录：Windows客户端连接Linux服务器'''
    global sleeptime
    global glog
    global debugLevel
    # 连接Telnet服务器
    tn = telnetlib.Telnet(Host, timeout=10)
    tn.set_debuglevel(debugLevel)

    # 输入登录用户名
    # finish = '请输入代号:'
    # print(finish)
    res = tn.read_until(b'\xc7\xeb\xca\xe4\xc8\xeb\xb4\xfa\xba\xc5:')
    print(res.decode('GBK'), file=glog, flush=True)
    tn.write(bytes(username + '\n', encoding = "utf8") )
    #
    # # 输入登录密码
    # finish="请输入密码:".encode("GBK")
    res = tn.read_until(b'\xc7\xeb\xca\xe4\xc8\xeb\xc3\xdc\xc2\xeb:')
    print(res.decode('GBK'), file=glog, flush=True)
    tn.write(bytes(password + '\n', encoding = "utf8") )

    try:  # 抓取OSError: [Errno 99] Cannot assign requested address  异常

        res = tn.read_until(b'\xb0\xb4 [RETURN] \xbc\xcc\xd0\xf8')
        print(res.decode('GBK'), file=glog, flush=True)
        tn.write(bytes('\n', encoding = "utf8") )
        print('1', file=glog, flush=True)

        res = tn.read_until(b'\xb0\xb4\xc8\xce\xba\xce\xbc\xfc\xbc\xcc\xd0\xf8 ..')
        print(res.decode('GBK'), file=glog, flush=True)
        tn.write(bytes('\n', encoding = "utf8") )
        print('2', file=glog, flush=True)

        res = tn.read_until(bytes(' ' + str(datetime.datetime.now().year) , encoding='utf8')+b'\x1b[K\x1b[C')
        print(res.decode('GBK'), file=glog, flush=True)
        tn.write(bytes('\n', encoding = "utf8") )
        print('3', file=glog, flush=True)

        res = tn.read_until(b'\xb0\xb4\xc8\xce\xd2\xe2\xbc\xfc\xbc\xcc\xd0\xf8...')
        print(res.decode('GBK'), file=glog, flush=True)
        tn.write(bytes('\n', encoding = "utf8") )
        print('4', file=glog, flush=True)

        res = tn.read_until(b'\n\x1b[K\n\x1b[K\n\x1b[K\n\x1b[K\n\x1b[K\n\x1b[K\n\x1b[K\x1b[24;20H')
        print(res.decode('GBK'), file=glog, flush=True)
        tn.write(bytes('\n', encoding = "utf8") )
        print('5', file=glog, flush=True)

        res = tn.read_until(b'(n)\xbc\xcc\xd0\xf8  [n]:')
        print(res.decode('GBK'), file=glog, flush=True)
        tn.write(bytes('\n', encoding = "utf8") )
        print('6', file=glog, flush=True)
    except Exception as link_fault:
        print(link_fault, file=glog, flush=True)
        exit(1)

    return tn

    # 按任何键继续 ..，　按 [RETURN] 继续，☆ 上次连线时间为 Sat Aug  4 13:51:12 2018
    # ，☆ 按任意键继续...  2次
    # 如何处理以上密码输入错误记录  (m)邮回信箱  (y)清除  (n)继续  [n]:

def do_cmd(tn, cmd,h,m):
    #        停留[  0:11]
    finish=b'\xcd\xa3\xc1\xf4[%3d:%d]\x1b[K\x1b[2;25H'%(h,m)
    # res = tn.read_until(finish)
    res = tn.read_some()
    # print(res.decode('GBK'))
    tn.write(bytes(cmd, encoding="utf8"))
    pass


def do_loop(username, password):
    global sleeptime
    global glog
    Host = 'bbs.newsmth.net'  # Telnet服务器IP
    tn  = do_telnet(Host, username, password)
    if tn is None:
        print("telnet link error", file=glog, flush=True)
        exit()
    print('++++++++++++++', file=glog, flush=True)

    print('link ok', file=glog, flush=True)
    print('keep live interval %d minutes'%(sleeptime/60), file=glog, flush=True)
    print('++++++++++++++', file=glog, flush=True)
    # 记录开始时间
    starttime = datetime.datetime.now()
    # ３分钟操作一次
    while(True):
        sleep(sleeptime)
        curMinutes=(datetime.datetime.now()-starttime).seconds/60
        try:  # 抓取OSError: [Errno 99] Cannot assign requested address  异常
            do_cmd(tn,"0",curMinutes/60,curMinutes%60)
            print('keep live','| login time[%d:%d]'%(curMinutes/60,curMinutes%60), file=glog, flush=True)
        except Exception as link_fault:
            print('login time[%d:%d]'%(curMinutes/60,curMinutes%60), file=glog, flush=True)
            print('do_cmd error: ',link_fault, file=glog, flush=True)
            break
    pass
    tn.close()  # tn.write('exit\n')

if __name__ == '__main__':
    global sleeptime
    global glog
    global debugLevel

    # finish="请输入密码:".encode("GBK")
    # print(finish)
    # assert False
    # 配置选项



    parse = OptionParser()

    parse.add_option("-u", "--username", action = "store",type="string",dest = "username", default="")
    parse.add_option("-p", "--password", action = "store",type="string",dest = "password", default="")
    parse.add_option("-l", "--log", action="store", type="string", dest="log", default="", help="日志输出，默认为终端")
    parse.add_option("-t", "--timeout", action="store", type="int", dest="timeout", default=3, help="单位分钟,请求间隔")
    parse.add_option("-d", "--debugLevel", action="store", type="int", dest="debugLevel", default=0, help="debug 级别　0-5")


    (option, arges) = parse.parse_args()
    if(len(option.username) == 0 or len(option.password) == 0):
        parse.print_help()
        exit()

    if(len(option.log) != 0):
        glog = open(option.log, 'a', encoding='utf8')

    print(type(option.timeout), option.timeout)
    sleeptime=60*option.timeout
    debugLevel=option.debugLevel

    while True:
        do_loop(option.username, option.password)
        sleep(sleeptime)