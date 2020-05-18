def user(**kwargs):
    return list(zip([kwargs], [kwargs.values()]))

print(user(name=input('Введите ваше имя: '), surname=input('Введите вашу фамилию: '),
           age=input('Введите ваш возраст: '), city=input('Введите город проживания: '),
           e_m=input('Введите ваш E-mail: '), tel=input('Введите ваш контактный номер: ')))


