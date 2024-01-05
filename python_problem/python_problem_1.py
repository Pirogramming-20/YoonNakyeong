import random
num = 0
end = True

def brGame(name,num):
    while end:
        try:
            n = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if (n != 1 and n != 2 and n != 3):
                print('1,2,3 중 하나를 입력하세요')
            else:
                break
        except ValueError:
            print('정수를 입력하세요')
    for i in range(n):
        num += 1
        print(name, num)
        if num >= 31:
            return num,False
    return num,True

while True:
    n=random.randint(1,3)
    for i in range(n):
        num += 1
        print('computer', num)
        if num >= 31:
            end=False
    if not end:
        print('player win!')
        break
    
    num,end = brGame('player',num)
    if not end:
        print('computer win!')
        break