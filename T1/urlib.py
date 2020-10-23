#-*- coding = utf-8 -*-
#@Author : FLin
#@Time : 2020/9/13 20:34
#@SoftWare : PyCharm
import urllib.request
import urllib.parse
# re=urllib.request.urlopen("http://www.baidu.com")
# print(re.read().decode('utf-8'))
# data=bytes(urllib.parse.urlencode({"name":"Lin","age":18}),encoding="utf-8")
# #data2=bytes(urllib.parse.urlencode(),encoding="utf-8")
#  re2=urllib.request.urlopen("",data=data2)
# re=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(re.read().decode("utf-8"))
# try:
#     re=urllib.request.urlopen("http://httpbin.org/get",timeout=10)
#     print(re.read().decode("utf-8"))
# except Exception:
#     print("timeout")
# re=urllib.request.urlopen("http://douban.com")
# print(re.getheader)
url="http://douban.com"
# url="http://httpbin.org/post"
data=bytes(urllib.parse.urlencode({"name":"p"}),encoding="utf_8")
header={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
# req=urllib.request.Request(url=url,data=data,headers=header)
req=urllib.request.Request(url=url,headers=header)
re=urllib.request.urlopen(req)
print(re.read().decode("utf-8"))
