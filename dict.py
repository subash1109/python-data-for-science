d={'2wheel':'bike','4wheel':'car','air':'plane'}

#print(d)

#print(d['air'])

#d['air']='aircraft'
#print(d)

#for i,j in d.items():
    #print(i,j)

#for i in d.keys():
    #print(i)

#for i in d.values():
    #print(i)

# simple calculator

a=int(input('enter the first num '))
b=int(input('enter the second num'))

choice =int(input('enter ur choice'))

d={1:a+b,2:a-b,3:a*b,4:a/b}

print(d[choice])

print(d)
