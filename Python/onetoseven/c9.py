
LIST = [3, 43, 89, 23, 45, 56, 78]
even = []
odd = []

while len(LIST) > 0:
    NUM = LIST.pop()
    if NUM % 2 == 0:
        even.append(NUM)
    else:
        odd.append(NUM)

print(even)
print(odd)
