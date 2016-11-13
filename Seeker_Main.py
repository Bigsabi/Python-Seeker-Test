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
'''
html = get_html(url_index)
print(html[:50])
'''

limit = get_limit()
print(limit)