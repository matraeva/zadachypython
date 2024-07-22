v = int(input('Номер места - '))

k = v/4

if v%4==0:
    print ('Номер купе -',int(k))
else:
    print ('Номер купе -',int(k+1))
