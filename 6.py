def my_func(text):
    result = []
    for i in range(len(text)):
        result.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(result)


print(my_func(input('Введите слова через пробел: ').split()))


