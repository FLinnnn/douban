#-*- coding = utf-8 -*-
#@Author : FLin
#@Time : 2020/9/13 18:55
#@SoftWare : PyCharm
#导包
from bs4 import BeautifulSoup #网页解析，获取数据
import re   #正则
import urllib.request,urllib.error  #给url 得数据
import xlwt  #excel
import sqlite3 #数据库
def main():
    baseurl="https://movie.douban.com/top250?start="
    savepath="豆瓣Top250.xls"
#爬取网页
    datalist=getData(baseurl)
    print(datalist)
#(逐一)解析数据

#保存数据
    saveDate(datalist,savepath)
    dbpath="movie.db"
    saveDate2DB(datalist,dbpath)
    print("over")
#创建正则规则，表示规则 链接规则
findlink=re.compile(r'<a href="(.*?)">')
#re.S包含换行符 图片
findImgSrc=re.compile(r'<img.*src="(.*?)".*/>',re.S)
#影片片名
findTitle=re.compile(r'<span class="title">(.*?)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq=re.compile(r'<span class="inq">(.*?)</span>')
#找到影片相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
def getData(baseurl):
    datalist=[]

    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askUrl(url)
        #逐一解析
        soup=BeautifulSoup(html,"html.parser")
        #查找符合要求的字符串，形成列表
        for item in soup.find_all('div',class_="item"):
            # print(item)
            #保存一部电影的所有信息
            data=[]
            item=str(item)
            #给个规则 正则表达式 获取链接
            link=re.findall(findlink,item)[0]
            data.append(link)
            # print(link)
            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            # print(imgSrc)
            # 标题
            titles=re.findall(findTitle,item)
            if(len(titles)==2):
                # 添加中文名
                ctitle=titles[0]
                data.append(ctitle)
                # 去掉无关符号
                # 添加外文名
                otitle=titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                # 为了数据库而留空 （如没有外文名）
                data.append(' ')


            # print(titles)
            # 打分
            rating=re.findall(findRating,item)[0]
            data.append(rating)
            # print(rating)
            # 评价人数
            judgeNum=re.findall(findJudge,item)[0]
            data.append(judgeNum)
            # print(judgeNum)
            #概述 (可能没有)
            inq=re.findall(findInq,item)
            if (len(inq)!=0):
                # 去掉句号
                inq=inq[0].replace("。","")
                data.append(inq)
            else:
                # 留空
                data.append(" ")
            # print(inq)
            #
            bd=re.findall(findBd,item)[0]
            # 去掉br等
            bd=re.sub('<br(\s+)?/>(\s+)?',"",bd)
            bd=re.sub('/','',bd)
            data.append(bd.strip())
            # print(Bd)
            datalist.append(data)


            #datalist.append(html)
    # print(datalist)
    return datalist
#得到一个指定url的网页内容
def askUrl(url):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"}
    #本质是告诉服务器，可以接受什么信息
    #模拟头部，模拟浏览器
    req=urllib.request.Request(url=url,headers=head)
    try:
        rep=urllib.request.urlopen(req)
        html=rep.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
def saveDate(datalist,path):


    # pass
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("豆瓣Top250",cell_overwrite_ok=True)
    col=("链接","图片","中文","外文","评分","评价人数","概述","相关")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for j in range(0,250):
        print("{}条目".format(j+1))
        data=datalist[j]
        for k in range(0,8):
            sheet.write(j+1,k,data[k])

    book.save(path)
def saveDate2DB(datalist,dbpath):
    # pass
    # init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cur=conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index==4 or index==5:
                continue
            else:
                data[index]='"'+data[index]+'"'
        sql='''
        INSERT INTO movie250(
        info_link,pic_link,cname,ename,score,rated,instroduction,info
        )VALUES (%s)
        '''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    # 创建数据表
    sql='''
    CREATE TABLE movie250
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    info_link test,
    pic_link text,
    cname VARCHAR,
    ename VARCHAR,
    score NUMERIC,
    rated NUMERIC,
    instroduction test,
    info text
    )
    '''
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # init_db("movietest")
    main()