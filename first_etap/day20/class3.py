f = input('Введите функуцию: ')

try:
    eval(f)
    print(eval(f))
except:
    print('Такой функции нет')
