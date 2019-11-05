''' 关键字可变参数 '''


def city_temp(**param):
    '''各个城市温度'''
    for key, value in param.items():
        print(key, ':', value)


CITY = {'bj': '20c', 'sh': '20', 'sz': '23c'}
city_temp(**CITY)
