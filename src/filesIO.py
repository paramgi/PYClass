# files IO in Python

# a = open('sample.txt','w')
# a.write('sdfalksdjflkja asdkjfhkasjd fsakjdhkasjdgh asdgkjasdhg ')
# a.close()

a = open('sample.txt','r')
# r1=a.read(48)
# # r1=a.readline()
# # r2=a.readline()
# print(r1)
# # print(r2)
# a.close()

# ====>>>  see and tell
pos1=a.read(48)
print(pos1)

pos2 = a.tell()
print(pos2)

txt1 = a.read()
print(txt1)

pos3= a.seek(34)
print(pos3)

# pos4=a.

a.close()





