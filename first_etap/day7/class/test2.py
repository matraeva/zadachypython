a = int(input('Введите число - '))


probels = a
simbols = 1
for i in range(1, a+1):
    print(' ' * probels + '*' * simbols)
    probels -= 1
    simbols += 2

for i in range(a+1, 0, -1):
    print(' ' * probels + '*' * simbols)
    probels += 1
    simbols -= 2
