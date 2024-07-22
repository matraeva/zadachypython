age = int(input('Введите ваш возраст - '))
money = int(input('Наличие денег - '))

if 18 <= age >= 55 or money >= 1000:
    print ('Welcome')
elif age > 55:
    print ('Уйди старый')
else:
    print ('get out here')

