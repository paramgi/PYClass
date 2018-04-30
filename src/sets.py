s1 = {1,2,3,4,5,6}
s2 = {2,3,1}
s1 = {s1 for s1 in range(1,10)}
print(s1)
s3 = frozenset(s1)
print(s3)
print(type(s3))

print(sum(s3))
print(min(s3))
print(max(s3))
print(all(s3))
print(len(s3))
print(any(s3))
# s3 = set()

# # print(type(s1))
# print(s1)

# s1.remove(1) -- work
# print(s1)
# print(s1.pop()) -- work

# print(s1.popitem()) -- not work

# s1.add('asd') -w
# s1.add(45)   -w

# s1.append() -nw
# s1.extend() -nw

# s1.update('asd','asdd')
print(s1)
# s1.update(['axxxsd','axxxsdd'])
# print(s1)
# s1.update({'asxxd','asdxxxxxd'})
# print (s1+s2)
# print (2*s1)

# print(s1-s2)
# print(s2-s1)

# print(s1|s2)

# print(s1&s2)

# print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s1.issuperset(s2))




# print(s1)