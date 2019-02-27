import requests
import re
import time
import subprocess

netspeed_log = {'time':[],
                'speed':[],
                'ping':{'baidu.com':[],
                        'ustc.edu.cn':[]},
                }

def get_teach_ustc_edu_cn(newhtml):
    teach_url = 'https://www.teach.ustc.edu.cn/'
    #更新教务处通知
    print('正在更新教务处通知')
    r = requests.get(teach_url)
    if r.status_code==200:
        news_content = re.findall('<section class="notice-fp">[\s\S]*?</section>', r.text)
        if news_content!=[]:
            news_content = news_content[0]
            newhtml = re.sub('<section class="notice-fp">[\s\S]*?</section>', news_content, newhtml)
            newhtml = re.sub('<section class="notice-fp">[\s\S]*?<header>[\s\S]*?</header>', '<section class="notice-fp">\n\t<header>\n<h2><a href="https://www.teach.ustc.edu.cn/category/notice">教务处通知</a></h2>\n\t<div style="height:3px;width:100%;display: block;background:#EEEEEE ;clear: both;"></div>\n</header>', newhtml)
            print('更新完成')
    else:
        print('网络错误：', r.status_code)
    return newhtml

def get_weather_com_cn(newhtml):
    url = 'http://www.weather.com.cn/weather/101220101.shtml'
    #更新天气
    print('正在更新天气信息')
    r = requests.get(url)
    if r.status_code==200:
        r.encoding = 'utf-8'
        new_content = re.findall('<ul class="t clearfix">[\s\S]*?</ul>', r.text)
        if new_content!=[]:
            new_content = new_content[0]
            newhtml = re.sub('<ul class="t clearfix">[\s\S]*?</ul>', new_content, newhtml)
            print('更新完成')
    else:
        print('网络错误：', r.status_code)
    return newhtml

def get_net_speed():
    #测试带宽
    print('正在测试带宽')
    url = 'http://test.ustc.edu.cn/'
    r = requests.get(url)
    speed = len(r.content)/r.elapsed.total_seconds()*8/1024/1024
    r = requests.get(url)
    speed = (speed + len(r.content)/r.elapsed.total_seconds()*8/1024/1024)/2
    print('测试完成')
    #测试ping
    print('正在测试ping')
    sites = ['baidu.com','ustc.edu.cn']
    for each in sites:
        p = subprocess.Popen('ping '+each, shell = True, stdout = subprocess.PIPE)
        p.wait()
        #print(p.stdout.read().decode('gbk'))
        netspeed_log['ping'][each].append( int(re.findall('平均 = (.*?)ms', p.stdout.read().decode('gbk'))[0]))
    print('测试完成')

    netspeed_log['time'].append(time.strftime("%H:%M", time.localtime()))
    netspeed_log['speed'].append(speed)

    if len(netspeed_log)>300:
        netspeed_log.pop(0)
    with open('webpage/static/js/netspeedandping.js', 'w', encoding='UTF-8') as dataf:
        dataf.write('var netspeeddata = '+str(netspeed_log)+';')

def getdata():
    f0 = open('webpage/index.html', 'r', encoding='UTF-8')
    newhtml = f0.read()
    f0.close()
    newhtml = get_teach_ustc_edu_cn(newhtml)
    newhtml = get_weather_com_cn(newhtml)
    get_net_speed()
    #print(newhtml)
    f = open('webpage/index.html', 'w', encoding='UTF-8')
    f.write(newhtml)
    f.close()
    