def div(a, b):
    try:
        return 'Результат деления = ', a / b
    except ZeroDivisionError:
        return 'Деление на 0'

print(div((int(input('Введите первое число: '))),
          (int(input('Введите второе число: ')))))