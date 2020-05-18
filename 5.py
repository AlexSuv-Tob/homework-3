def add():
    res = 0

    while True:
        numbers = input('Введите список цифр, для выхода нажмите *: ').split()
        for i in numbers:
            if i == '*':
                print(f'Сумма чисел равна {res}')

                return
            else:
                res += int(i)

        print(f'Сумма чисел  {res}. Выход')

add()
