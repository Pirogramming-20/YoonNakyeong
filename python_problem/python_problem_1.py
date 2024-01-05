num=0
while True:
    try:
        n=int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if (n!=1 and n!=2 and n!=3):
            print('1,2,3 중 하나를 입력하세요')
        else:
            break
    except ValueError:
        print('정수를 입력하세요')
for i in range(n):
    num+=1
    print('playerA :', num)