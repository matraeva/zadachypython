#1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i > 5:
        print (i)


#2
digits = (113, 118, -5, 1, 135, 137, 0, 142, 144, 17, 154, 0, 155, 2, 159, 172)

for i in digits:
    print (i/9)

#3
spisok_1 = set(('Lamborgini', 17, 4456, 2020, 'Paris', 'USA', 11, 23))
spisok_2 = set(('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23))

print(spisok_2.difference(spisok_1))



#Задание 1

for i in range(300):
    if i == 237:
        break
    if i % 2 == 0:
        print (i)

#Задание 2

text = []
while True:
   print ('Введите текст')
   t = input().split()
   if len(t) >= 6:
       text = t
       break
polovina = len(text) // 2 + (len(text) % 2)
temp1 = text[:polovina]
temp2 = text[polovina:]
result = temp2 + temp1

print (result)

#задание 3

even = 0
add = 0

for i in numbers:
    if i % 2 ==0:
        even += 1
    else:
        odd += 1
print (even, odd)

print (len([i for in numbers if i % 2 ==0]))
print (len([i for i numbers if i % 2 != 0]))



