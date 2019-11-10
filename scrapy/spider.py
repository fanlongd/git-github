'''
爬虫前奏：

1、明确目的
2、找到数据对应的网页
3、分析王爷的结构找到数据所在标签位置
4、模拟HTTP请求，向服务器发送这个请求，获取到服务器返回给我们的HTML
5、用正则表达式提取我们需要的数据
'''

import re
import pandas as pd
from urllib import request


class Spider():
    url = 'https://sz.ke.com/ershoufang/pg3/'     # 贝壳网深圳二手房网页
    
    # 正则表达式
    root_pattern = r'<li class="clear">([\s\S]*?)</li>'  # 根表达式——房产信息
    position_pattern = r'/">([\s\S]*?)</a>'                   # 位置信息
    totalprice_pattern1 = r'<div class="totalPrice"><span>([\s\S]*?)</div>'  
    totalprice_pattern = r'([^</span>])'                           # 总价进一步信息
    unitprice_pattern = r'<span>单价([\s\S]*?)</span>'              # 单价信息

    def __fetch_content(self):
        '''
        抓取网页数据，转换成字符穿代码
        '''
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    
    def __analysis(self, htmls):
        '''
        利用正则表达式分析数据，逐层分析法。获得的数据已字典形式存入列表
        '''
        root_info = re.findall(Spider.root_pattern, htmls)
        houses = []
        for info in root_info:
            position = re.findall(Spider.position_pattern, info)
            totalprice1 = re.findall(Spider.totalprice_pattern1, info)
            totalprice = ''.join(totalprice1)
            totalprice = re.findall(Spider.totalprice_pattern, totalprice)
            totalprice = ''.join(totalprice)
            totalprice = [totalprice]
            unitprice = re.findall(Spider.unitprice_pattern, info)
            house = {
                    '位置': position, '总价': totalprice, 
                    '单价': unitprice
                    }
            houses.append(house)
        return houses

    def __refine(self, houses):
        '''
        精炼数据列表，本例实现'[]'符号的删除
        '''
        h = lambda house: {
                '位置': house['位置'][0].strip(),
                '总价': house['总价'][0].strip(),
                '单价': house['单价'][0].strip()
        }
        return map(h, houses)

    def __sort(self, houses):
        '''
        列表元素按关键字排序
        '''
        houses = sorted(houses, key=self.__sort_seed, reverse=True)
        return houses

    def __sort_seed(self, house):
        '''
        设定排序关键字
        '''
        r = re.findall('\d*', house['总价'])
        num = float(r[0])
        if '万' in house['总价']:
            num *= 10000
        return num

    def __show(self, houses):
        '''
        houses列表转换成DataFrame格式，并实例化该变量
        '''
        self.houses = pd.DataFrame(houses)
        
    def go(self):
        '''
        定义go函数，放置以上实例方法，方便外部调用
        '''
        htmls = self.__fetch_content()
        houses = self.__analysis(htmls)
        houses = list(self.__refine(houses))
        houses = self.__sort(houses)
        self.__show(houses)


spider = Spider()
spider.go()
print(spider.houses)
print(type(spider.houses))
# 保存到excel
spider.houses.to_excel('./data/spider.xls', sheet_name='Sheet1')  