
import re

S = 'life is short, i use python, i love python'
r = re.match('life(.*)python(.*)python', S)
print(r.group(0))
print(r.group(1))
print(r.group(2))

r1 = re.findall('life(.*)python(.*)python', S)
print(r1)
