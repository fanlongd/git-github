'''
爬虫改进版：

1、引入Beautifulsoup4包，简化正则表达式
2、利用url特点，多页抓取
3、将抓取str格式转成json交换格式
4、类封装
'''

import requests
import json
import pandas as pd
from bs4 import BeautifulSoup


class Beike(object):
    def __init__(self):
        self.url = 'https://sz.ke.com/ershoufang/'
        self.result_list = []

    def start_requests(self, url):
        r = requests.get(url)
        return r.content

    def parse(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        house_list = soup.find_all('li', class_='clear')

        for house in house_list:
            mydict = {}
            position = house.find('div', class_='positionInfo')
            mydict['position'] = position.find('a').text
            unitPrice = house.find('div', class_='unitPrice')
            mydict['unitPrice'] = unitPrice.find('span').text
            mydict['totalPrice'] = house.find('div', class_='totalPrice').text
            self.result_list.append(mydict)

    def write_json(self, result):
        houses = json.dumps(result, indent=4, ensure_ascii=False)
        with open('./data/houses.json', 'w', encoding='utf-8') as f:
            f.write(houses)

    def start(self):
        for i in range(0, 10):
            self.url = 'https://sz.ke.com/ershoufang/pg{}/'.format(i)
            text = self.start_requests(self.url)
            self.parse(text)
            self.write_json(self.result_list)
           

beike = Beike()
beike.start()
h = pd.DataFrame(beike.result_list)
h.to_excel('./data/houses.xls')
