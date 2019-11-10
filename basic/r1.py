
# 正则表达式
# 正则表达式是一个特殊字符串，用于判断给定字符串是否与所操作的字符串相符
# 爬虫

import re

S = '68B8CjdD45E8F'

a = re.match('\d', S)
print(a.span())
a1 = re.search('\d', S)
print(a1.group())
a2 = re.findall('\d', S)
print(a2)
