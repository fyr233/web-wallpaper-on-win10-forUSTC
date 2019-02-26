import requests
import re

teach_url = 'https://www.teach.ustc.edu.cn/'

def getdata():
    f0 = open('webpage/index.html', 'r', encoding='UTF-8')
    newhtml = f0.read()
    f0.close()
    f = open('webpage/index.html', 'w', encoding='UTF-8')
    #更新教务处通知
    print('正在更新教务处通知')
    r = requests.get(teach_url)
    if r.status_code==200:
        news_content = re.findall('<section class="notice-fp">[\s\S]*?</section>', r.text)
        if news_content!=[]:
            news_content = news_content[0]
            newhtml = re.sub('<section class="notice-fp">[\s\S]*?</section>', news_content, newhtml)
            newhtml = re.sub('<section class="notice-fp">[\s\S]*?<header>[\s\S]*?</header>', '<section class="notice-fp">\n\t<header>\n<h2><a href="https://www.teach.ustc.edu.cn/category/notice">教务处通知</a></h2>\n\t<div style="height:3px;width:100%;display: block;background:#EEEEEE ;clear: both;"></div>\n</header>', newhtml)
            
    else:
        print('网络错误：', r.status_code)
    f.write(newhtml)
    f.close()
    