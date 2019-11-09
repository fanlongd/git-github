'''
for in 遍历循环
while 条件循环
'''

# for letter in 'Python':
#     print('当前字母：' + letter)
# else:
#     pass


# STR = 'i love Python'
# for index in range(len(STR)):
#     print(STR[index])
# else:
#     pass


# 找出2-100的素数个数，并打印所有素数
# 方法1.

# import time

# START = time.time()

# count = 0
# sum = 0

# for i in range(2, 10000):
#     for i_x in range(2, i):
#         if i % i_x == 0:
#             break
#     else:
#         # print(i, 'is prime')
#         count += 1
#         sum += i

# print('Count of prime numbers:', count)
# print('Sum of prime numbers:', sum)

# END = time.time()
# print('Running time:', END - START)


# 方法2.

# count = 0
# i = 2

# while i < 100:
#     x = 2
#     while x <= i/x:
#         if not (i % x):
#             break
#         x += 1
#     if x > i/x:
#         print(i, 'is prime')
#         count += 1
#     i += 1
# print('Total is:', count)
