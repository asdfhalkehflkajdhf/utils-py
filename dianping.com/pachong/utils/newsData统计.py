# -*- coding: utf-8 -*-   

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root',root)  # 当前目录路径
        print('dirs',dirs)  # 当前路径下所有子目录
        print('files',files)  # 当前路径下所有非目录子文件
        print('============')

def file_list(dir):
    # 只获取目录

    dirs = os.listdir( dir )
    for dir_i in dirs:
        file_dir=os.path.join(dir,dir_i)
        file_name(file_dir)
    # 输出所有文件和文件夹
    for file in dirs:
       print (file)

def getNewsDataPathList(dirPath,start=None, end=None):
    resList=[]
    table_dirs = os.listdir(dirPath)
    for dir_i in table_dirs:
        if start is not None:
            if dir_i<start:
                continue
        if end is not None:
            if dir_i>end:
                continue
        file_dir = os.path.join(dirPath,dir_i)
        for root, dirs, files in os.walk(file_dir):
            if len(files)!=0:
                for fileName in files:
                    tp = os.path.join(root,fileName)
                    resList.append(tp)
    return resList

def getNewsDataStatInfo(dirPath):
    table_dirs = os.listdir(dirPath)
    print('有表个数：',len(table_dirs))
    totleFileNum=0
    for dir_i in table_dirs:
        file_dir = os.path.join(dirPath,dir_i)
        for root, dirs, files in os.walk(file_dir):
            # if len(files)!=0:
                print('\t',root,'\t','表：',dir_i,'有文章数：',len(files))
                totleFileNum+=len(files)
    print('有文章总数：',totleFileNum)


if __name__ == '__main__':
    # file_name('newsData')
    # file_list('newsData')

    getNewsDataStatInfo('../newsData')

    res = getNewsDataPathList('../newsData')
    print(res)
    f = open(res[0], 'r', encoding='utf8')
    r = f.read()
    print(r)