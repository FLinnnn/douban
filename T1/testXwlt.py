#-*- coding = utf-8 -*-
#@Author : FLin
#@Time : 2020/9/23 22:06
#@SoftWare : PyCharm
import xlwt
'''
# 创建workbook对象
workbook=xlwt.Workbook(encoding="utf-8")
# 创建工作表
worksheet=workbook.add_sheet("sheet1")
# 一行二列三内容
worksheet.write(0,0,'hello')
# 保存
workbook.save('test.xls')
'''
workbook=xlwt.Workbook(encoding="utf-8")
worksheet=workbook.add_sheet("sheet1")
for i in range(1,10):
    for j in range(1,i+1):
        worksheet.write(i-1,j-1,"{} * {} = {}".format(i,j,(i*j)))
workbook.save('test.xls')