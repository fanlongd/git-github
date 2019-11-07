

def BMI(height, weight):
    h = height
    w = weight
    h = float(height)
    w = float(weight)

    BMI = w/(h**2)

    if BMI < 18.5:
        print('过轻')
    elif 18.5 <= BMI <= 25:
        print('正常')
    elif BMI > 25:
        print('过重')
    else:
        print('严重肥胖')


Xiaoming = BMI(1.75, 80)

