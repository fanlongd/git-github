'''
引入pandas
将爬虫获取的字典数据转成DataFrame
DataFrame写入excel文件
'''

import xlwt
from spider import Spider

spider = Spider()
spider.go()
print(spider.houses)
print(type(spider.houses))
# 保存到excel
spider.houses.to_excel('./advance/houses.xls', sheet_name='Sheet1')  