
# order of Arguments
# positional, default, arbitory


# def add():
# 	a=1
# 	b=4
# 	return a+b

# add()
# print(add())


# Arguments 
#	1 positional

# def add(a,b):
# 	print(a*b)

# a=int(input('enter a number for a\n'))
# b=int(input('enter a number for b\n'))
# add(a,b)


#	2  default

# def add(a=1,b=2):
# 	print(a+b)

# a=int(input('enter a number for a\n'))
# b=int(input('enter a number for b\n'))
# add()
# add(a)
# add(a,b)

# keyword

# def add(a,b):
# 	print(a+b)

# add(a=9,b=98)

# arbitary means Random


def arb(*names):
	print(names)
	print(type(names))
	for a in names:
		print('welcome',a, 'to world')
		
arb('vin','cl')


def Gre(**details):
	print(details)
	print(type(details))
	for name,place in details.items():
		print('welcome',name,'sdfsdf ', place)

Gre(vin='hyd',sup='usa',bat='la')


# local and global variables

a=1
def f1():
	global a
	a=2
	print(a)
def f2():
	a=3
	print(a)
def f3():
	a=20
	print(a)
def f4():
	a=23
	print(a)
	# global a
	print(a)

print(a)
f1()
f2()
print(a)
f3()
f4()

# lambda is keyword
# Syntax    >>>>   variable name = lambda arg : espression

# add = lambda a,b:a**b
# # print(add(9,12))

# add = lambda a,b:[print(a**i) for i in range(1,b) ]
# add(91,12)


# add = lambda *a:[print(name) for name in a]
# add('s','w','sdf')


