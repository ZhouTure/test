import requests
from bs4 import BeautifulSoup
import re
import sys


input_name = input('请输入你要生成的姓名\n')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
url = "http://www.uustv.com/"
query_data = {
    "word": input_name,
    "sizes": "60",
    "fonts": "1.ttf",
    "fontcolor": "#000000"
}
response = requests.post(url, data=query_data, headers=headers)
# print(response.status_code)
text = response.content.decode()
# print(text)
soup = BeautifulSoup(text, 'html.parser')
all_img = soup.find_all('div', class_='tu')
result1 = re.findall(r'<div class="tu">﻿<img src="(.*)"/></div>', str(all_img[0]))
url1 = url + result1[0]
mdir = sys.path[0] + '/'
with open(mdir + input_name + '的个性签名.jpg', 'wb') as f:
    f.write(requests.get(url1).content)
