score = int (input ('Оценка - '))

if score >= 100:
    print ('Оценка A')
else: 
   if score >= 70:
        print ('Оценка B')
   else:
        if 70 > score >= 50:
            print ('Оценка C')
        else:
            print ('Пересдача!')
