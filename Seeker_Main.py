import re
from urllib.request import urlopen
import urllib
import os

gConst = {
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'DNT':'1',
    'Host':'jandan.net',
    'Upgrade-Insecure-Requests':'1',
    'Cookie':'jdna=01b0531fab6a989460dd1b231010b496#1479450267836; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1479449506; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1479450268; _ga=GA1.2.71180035.1479449506',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

url_index="http://jandan.net/ooxx"
url_head="http://jandan.net/ooxx/page-"

#获取指定链接地址
def get_html(url):
    req = urllib.request.Request(url,None,gConst)
    html = urlopen(req).read().decode()
    return html
#获取最大页码
def get_maxpage(url=url_index):
    html=get_html(url)
    pattern = re.compile(r'<span class="current-comment-page">\[(\d+)\]</span>')
    limit = pattern.findall(html)
    return limit[0]

#获取这个页面所有的图片
def get_imgs(url):
    html = get_html(url)
    pattern = re.compile(r"[a-zA-z]+://[^\s]*\.jpg")
    imgs = pattern.findall(html)
    return imgs

def download_imgs(imgs,nowPage):
    img_set = set(imgs)
    imgs = list(img_set)
    dicName = "./JIANDAN/"+str(nowPage);
    if not os.path.exists(dicName):
        os.makedirs(dicName)
    for i in range(len(imgs)):
        img_url = imgs[i]
        try:
            img_data = urlopen(img_url).read()
        except:
            continue
        with open(dicName+"/"+str(i)+'.jpg','wb') as f:
            f.write(img_data)
limit = int(get_maxpage())
for i in range(limit+1)[::-1]:
    print(str(i)+"/"+str(limit)+"Url:"+url_head+str(i));
    imgs = [];
    try:
        imgs = get_imgs(url_head+str(i))
        download_imgs(imgs,i)
    except:
        continue;
    print(imgs)
# '''
# html = get_html(url_index)
# print(html[:50])
# '''
# #[a-zA-z]+://[^\s]*\.jpg
# #limit = get_limit()
# #print(limit)
# imgs =get_imgs(url_index) 
# #print(get_imgs(url_index))
# download_imgs(imgs)
