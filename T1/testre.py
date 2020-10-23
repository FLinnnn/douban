#-*- coding = utf-8 -*-
#@Author : FLin
#@Time : 2020/9/18 21:32
#@SoftWare : PyCharm
#正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re
#创建模式对象
#search 只会找到第一个目标
# ex=re.compile("AA")
#正则
# m=ex.search("AAaaAA")
#校验目标

# print(m)
# m.group()
# print(m.group())
#没有模式对象（简写）
#前面是正则，后面是校验目标
# m=re.search("AA","AAASS")
# print(m)

#findall(简写)
#查出所有放到列表list
# r=re.findall("[a-b]+","cabacbbaaaa")
# print(r)

#sub 1被替换 2替换着 3目标
print(re.sub("a","A","aaacAAs"))
#建议在正则表达式，被比较字符串前面加上r （转义问题）