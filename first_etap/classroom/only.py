flag = True
for i in range(10):
    i = int(input())
    if i % 2 != 0:
        flag = False
if flag == False:
    print('NO')
else:
    print('YES')
