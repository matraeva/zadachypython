n1 = int(input('Первое число: '))
n2 = int(input('Второе число: '))
n3 = int(input('Третье число: '))
n4 = int(input('Четвертое число: '))

if n1<n2<n3<n4:
    print (n1)
elif n2<n1<n3<n4:
    print (n2)
elif n3<n1<n2<n4:
    print (n3)
else:
    print (n4)

