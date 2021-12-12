
def greeting(name,animal=''):
    print('happy new year',name.title())
    print('this is animal ',animal.title())



#postional aruguments

#greeting(animal='dog',name='jhon')

# default
#greeting('jhon','cat')

#opttionl

#greeting('jhon')


# simple calculator

def add_(a,b):
    print(a+b)

def sub_(a,b):
    print(a-b)

def mul_(a,b):
    print(a*b)

def div_(a,b):
    print(a/b)

while True :
    a=int(input  ('enter the first num :'))
    b=int(input  ('enter the sec num :'))

    choice=int(input('enter the choice'))

    if choice == 1:
        add_(a,b)
    elif choice == 2:
        sub_(a,b)
    elif choice == 3:
        mul_(a,b)
    elif choice == 4:
        div_(a,b)
    else :
        print('calculator exited')
        break
