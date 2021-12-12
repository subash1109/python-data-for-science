
# return

def add(a):
    sum=0
    a[0]=5
    for i in a:
        sum=sum+i
    return sum

def print_dict(d):
    for i,j in d.items():
        print(i,j)
#print(add(5,6))
a=[1,3,5]
print(add(a[:]))
print(a)

d={ 'a':'apple','b':'ball'}
print_dict(d)

def add_n_numbers(*a):
    sum=0
    for i in a:
        sum=sum+i

    return sum

print(add_n_numbers(5,6,6,8))        
