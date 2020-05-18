def max_sum(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    return 'Результат сложения двух наибольших чсел равен: ', sum(my_list)

print(max_sum(int(input('Введите первое число: ')),
      int(input('Введите второе число: ')),
      int(input('Введите третье число: '))))



