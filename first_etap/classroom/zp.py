o = int(input('Введите оклад работника - '))
dk = 21 
df = int(input('Количество фактически отработанных дней - '))
p = int(input('Премия или надбавка - '))
n = 13
u = int(input('Удежания и штрафы - '))

zp = (o/dk*df+p)*((100-n)/100)-u
print (zp)

