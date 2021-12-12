
from simplecal import Simple_cal as S

while True :
    print('1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.QUIT\n')
    choice=int(input())
    if choice == 5:
        print('calculator is exited')
        break
    a=int(input('enter a 1 num'))
    b=int(input('enter a 2 num'))

    s=S(a,b)
    if choice == 1:
        s.add()
    elif choice == 2:
        s.sub()
    elif choice == 3:
        s.mul()
    elif choice == 4:
        s.div()
