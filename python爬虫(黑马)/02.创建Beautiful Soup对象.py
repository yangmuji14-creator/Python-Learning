# 导入模块
from bs4 import BeautifulSoup

# 创建Beautiful Soup对象
soup = BeautifulSoup('<html>data</html>','lxml')
print(soup)