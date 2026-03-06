import urllib.request
import re
import urllib.parse
query = urllib.parse.quote('贵阳 野人先生 冰淇淋')
url = f'https://cn.bing.com/images/search?q={query}'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    murls = re.findall(r'murl&quot;:&quot;(.*?)&quot;', html)
    for m in murls[:10]:
        print(m)
except Exception as e:
    print('Error:', e)
