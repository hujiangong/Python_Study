#!usr/bin/env python
# coding:utf-8

import re
import os
import time
import xlwt

def reSearch( parten, content, num=1):
    resault = ''
    if re.search(parten, content):
        resault = re.search(parten, content).group(num)
    return resault

def strFormat(arg):
    #arg = ''.join(arg.split())
    arg = ''.join(arg.strip().split('\n'))
    return arg

def urlFormatUtils(self, url=''):
    if url != '':

        # 格式化url
        url = 'http:%s' % url if 'http' not in url else url
        url = url.split('#')[0] if '#' in url else url
        url = url.split('?')[0] if '?' in url else url
    return url

def timeFormat(dt,Format=''):
    #"%Y-%m-%d %H:%M:%S"

    if '发布时间：' in dt:
        timestamp = re.sub('发布时间：','',dt)
        return timestamp
    #duration 处理
    if Format == '':
        t = dt.split(':')
        if len(t) == 2:
            timestamp =  int(t[0]) * 60 + int(t[1])
        elif len(t) ==3:
            timestamp = int(t[0]) * 60 * 60 + int(t[1]) * 60 + int(t[2])
        elif len(t) == 0 or dt == '':
            return 0
    #uploadtime 时间处理
    elif '小时' in dt:
        #小时前 小时内
        h =  reSearch('\d+', dt, 0)
        timestamp = int(time.time() - int(h) * 60 * 60)
    else:
        timeArray = time.strptime(dt, Format)
        timestamp = int(time.mktime(timeArray))
    return timestamp

def resaultW_fromat(content):
    res = reSearch('\d+.\d+', content, 0)
    if res != '':
        if "万" in content or u'\u4e07' in content:
            res = int(float(res) * 10000)
        if "千" in content:
            res = int(float(res) * 10000)
    else:
        res = 0
    return res

def write_exal(filename,content,encode='utf8'):

    newf = os.path.join('exe',filename)
    workbook = xlwt.Workbook(encode)
    worksheet = workbook.add_sheet(filename)
    worksheet.write(0, 0, label='name')
    worksheet.write(0, 1, label='duration')
    worksheet.write(0, 2, label='play_times')
    worksheet.write(0, 3, label='release_time')
    worksheet.write(0, 4, label='url')
    worksheet.write(0, 5, label='relaser')
    worksheet.write(0, 6, label='channel')
    i =0
    for k in content:
        for a in range(len(content[k])):
            i +=1
            worksheet.write(i, 0, label=content[k][a][0])
            worksheet.write(i, 1, label=content[k][a][1])
            worksheet.write(i, 2, label=content[k][a][2])
            worksheet.write(i, 3, label=content[k][a][3])
            worksheet.write(i, 4, label=content[k][a][4])
            worksheet.write(i, 5, label=content[k][a][5])
            worksheet.write(i, 6, label=k)
    workbook.save('%s.xls'%newf)

