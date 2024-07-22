i = input('Действие: ')
a = int(input('Введите 1 число:'))
b = int(input('Введите 2 число:'))

while True:
 if i == '+':
     print (a+b)
 elif i == '-':
     print (a-b)
 elif i == '*':
     print (a*b)
 elif i == '/':
     print (a/b)
 elif i == '/' and b == 0:
     print ('На ноль делить нельзя!')
 else:
     break
