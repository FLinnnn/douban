#-*- coding = utf-8 -*-
#@Author : FLin
#@Time : 2020/9/16 20:57
#@SoftWare : PyCharm
#转化为树形结构
#Tag
#Navigablestring
#Beautifulsoup
#Comment
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
url="http://baidu.com"
data=bytes(urllib.parse.urlencode({"name":"p"}),encoding="utf_8")
header={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
req=urllib.request.Request(url=url,headers=header)
re=urllib.request.urlopen(req)
# print(re.read().decode("utf-8"))
html=re.read().decode("utf-8")
bs=BeautifulSoup(html,"html.parser")
#1  Tag 标签及其内容，拿到它找到的第一个内容
# print(bs.a)
# #第一个a
#
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(bs.div)
# print(bs.a)
#2  NavigableString 标签里的内容 .text
# print(bs.title.string)
# print(bs.a.attrs)
#3  BeautifulSoup 整个文档对象
# print(bs)
#4  注释comment 特殊的navigablestring 不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))


#————————————————————
#文档遍历
# print(bs.head.contents)
# print(bs.head.contents[1])
#文档搜索
# (1 find_all()
# 字符串过滤：会查找与字符串完全匹配的内容

# t_list=bs.find_all("a")
import re
# 正则表达式 search()方法匹配
# t_list=bs.find_all(re.compile(".?.?a.?"))
# 方法：传入一个函数(方法)，根据函数的要求来搜索
# def name(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name)
# for item in t_list:
#     print(item)
# print(t_list)
# (2 kwargs 参数
# t_list=bs.find_all(id="head")
# t_list=bs.find_all(class_=True)
# (3 text 参数
# t_list=bs.find_all(text="网页")
#通过正则查找包含特定文本的内容
# t_list=bs.find_all(text=re.compile("网"))
# (4 limit 参数
#数量限制
# t_list=bs.find_all("a",limit=3)
# 选择器CSS
#通过标签
t_list=bs.select("title")
#通过类名
# t_list=bs.select(".xxx")
#通过id
# t_list=bs.select("#xxx")
#通过属性
# t_list=bs.select("a[class='']")
#通过父子结构
# t_list=bs.select("head > title")
#通过兄弟节点
# t_list=bs.select(".cccc ~ .AAAAA")
#get_text()
# print(t_list)



