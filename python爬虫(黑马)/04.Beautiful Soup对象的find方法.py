# 1.导入模块
from bs4 import BeautifulSoup

# 2.准备文档字符串
html = '''<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
</body>
</html>'''
# 3.创建Beautiful Soup对象
soup = BeautifulSoup(html,'lxml')

# 4.查找title标签
title = soup.find('title')
print(title)

# 5.查找 a 标签
a = soup.find('a')
print(a)

# 查找所有的a标签
a_s = soup.find_all('a')
print(a_s)