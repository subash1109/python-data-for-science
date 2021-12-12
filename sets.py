#sets

s={3,4,6}
a=set([1,1,8,3])

#print(a)

a.add(5)
print(a)

# union

print(a.union(s))

print(a.intersection(s))

a=frozenset([1,4,66])
