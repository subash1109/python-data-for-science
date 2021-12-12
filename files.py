
with open('names.txt') as ptr:
    conent=ptr.read()

print(conent)

with open('names.txt','w') as ptr:
    ptr.write('jai')

    
