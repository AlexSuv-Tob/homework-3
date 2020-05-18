# 1 способ
def my_func(x, y):
    return x ** abs(y)
print(my_func(int(input('Введите возводимое число: ')),
              int(input('Введите степень возведения числа: '))))

#2 способ
def my_func1(x, y):
    j = x
    for i in range(abs(y) - 1):
        x *= j

    return x

print(my_func1(int(input('Введите возводимое число: ')),
              int(input('Введите степень возведения числа: '))))
