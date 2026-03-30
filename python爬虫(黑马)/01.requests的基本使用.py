# # 1.导入模块
# import requests
#
# # 2.发送请求
# response = requests.get('http://www.baidu.com')
# # print(response.text)
# # 3.获取响应数据
# response.encoding = 'utf-8'                         # 设置编码为 UTF-8
# print(response.text)
#
# # 打印响应的二进制数据
# print(response.content)
# # 把二进制数据转换成字符串
# print(response.content.decode())


# 案例：
    # 获取丁香园新型冠状病毒肺炎疫情实时动态首页内容
    # 首页URL为：https://ncov.dxy.cn/ncovh5/view/pnemonia


# 复习：定义分割线函数
def splitLines():
    print("-------------------------------------------------------------------------")


# 1.导入模块
import requests

# 2.发送请求
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pnemonia')

# 3.获取响应数据
# 设置编码为utf8
response.encoding = 'utf8'
print(response.text)

splitLines()

# 打印二进制数据
print(response.content)

splitLines()

# 将响应的数据转换成字符串
print(response.content.decode())
