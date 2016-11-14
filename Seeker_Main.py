from urllib.request import urlopen

import re

url_index="http://jandan.net/ooxx"
url_head="http://jandan.net/ooxx/page-"

def get_html(url):
    html = urlopen(url).read().decode()
    return html
def get_limit(url=url_index):
    html=get_html(url)
    pattern = re.compile(r'<span class="current-comment-page">\[(\d+)\]</span>')
    limit = pattern.findall(html)
    return limit[0]
def get_imgs(url):
    html = get_html(url)
    pattern = re.compile(r"[a-zA-z]+://[^\s]*\.jpg")
    imgs = pattern.findall(html)
    return imgs
def download_imgs(imgs):
    img_set = set(imgs)
    imgs = list(img_set)
    for i in range(len(imgs)):
        img_url = imgs[i]
        #img_data = urlopen(img_url).read() 
        try:
            img_data = urlopen(img_url).read()
        except:
            continue
        with open(str(i)+'.jpg','wb') as f:
            f.write(img_data)
'''
html = get_html(url_index)
print(html[:50])
'''
#[a-zA-z]+://[^\s]*\.jpg
#limit = get_limit()
#print(limit)
imgs =get_imgs(url_index) 
#print(get_imgs(url_index))
download_imgs(imgs)
