age = int(input('Возраст: ')) 
opyt = int(input('Опыт работы: '))
money = int(input('Желаемая зарплата: '))
language = input('Язык программирования: ')

if language.lower() == 'java' or language.lower() == 'javascript' or language.lower() == 'python':
    if 65 < age > 18:
        if opyt >= 3:
            if money >= 60000:
                 print ('Вы приняты на работу!')
else:
    print ('К сожалению, ваша кандидатура не подходит.')
