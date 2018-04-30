

def Assop(b,x):
	if b==1:
		x = x
	elif b==2:		
		x += x
	elif b==3:		
		x -= x
	elif b==4:		
		x *= x
	elif b==5:		
		x /= x
	elif b==6:		
		x %= x
	elif b==7:		
		x //= x
	elif b==8:		
		x **= x
	elif b==9:		
		x &= x
	elif b==10:		
		x |= x
	elif b==11:		
		x ^= x
	elif b==12:		
		x >>= x
	elif b==13:		
		x <<= x
	else:
		print('invalid number entered for operator')
	print(x)
#'operator'
#'Enter the number for operator'
# count = 0
# while (count < 9):
#    print 'The count is:', count
#    count = count + 1

a=1
while (a>0):
	print ('Enter the number for operator')
	print ('1 -> Arithmetic operators')
	print ('2 -> Comparison operators')
	print ('3 -> Logical operators')
	print ('4 -> Bitwise operators')
	print ('5 -> Assignment operators')
	print ('6 -> Identity operators')
	print ('7 -> Membership operators')
	print ('0 -> Exit')
	a = int(input('Please enter a number'))

	if (a==1):
		print ('\n' * 50)
		print('                 --> Enter the number for Arithmetic operator <--')
		print ('1 -> +   Add')
		print ('2 -> -   Subtract ')
		print ('3 -> *   Multiply ')
		print ('4 -> /   Divide ')
		print ('5 -> %   Modulus ')
		print ('6 -> //  Floor division')
		print ('7 -> **  Exponent ')
		print ('0 -> Exit')
		b = int(input('---> Please enter a number <--'))
		if(b==1):
			x = int(input('end the value of x'))
			y = int(input('end the value of x'))
			print ('\n' * 50)	
			print('addition of x and y is ',x+y)
		elif(b==2):
			x = int(input('end the value of x'))
			y = int(input('end the value of x'))
			print ('\n' * 50)	
			print('Subtract of x and y is ',x-y)
		elif(b==3):
			x = int(input('end the value of x'))
			y = int(input('end the value of x'))
			print ('\n' * 50)	
			print('Multiply of x and y is ',x*y)
		elif(b==4):
			x = int(input('end the value of x'))
			y = int(input('end the value of x'))
			print ('\n' * 50)	
			print('Divide of x and y is ',x/y)
		elif(b==5):
			x = int(input('end the value of x'))
			y = int(input('end the value of x'))
			print ('\n' * 50)	
			print('Modulus of x and y is ',x%y)
		elif(b==6):
			x = int(input('end the value of x'))
			y = int(input('end the value of x'))
			print ('\n' * 50)	
			print('Floor division of x and y is ',x//y)
		elif(b==7):
			x = int(input('end the value of x'))
			y = int(input('end the value of x'))
			print ('\n' * 50)	
			print('Exponent of x and y is ',x**y)
		else:
			b=0

	elif(a==2):
		print('                 --> Enter the number for Comparison operators <--')
		print ('1 -> >   Greater that')
		print ('2 -> <   Less that ')
		print ('3 -> ==  Equal to ')
		print ('4 -> !=  Not equal to ')
		print ('0 -> Exit')
		b = int(input('---> Please enter a number <--'))
		if(b==1):
			x = int(input('end the value of x'))
			y = int(input('end the value of y'))
			print ('\n' * 50)
			if (x > y):
				print('x Greater that y ',x,'>',y,x>y)
			else:
				print('x not Greater then y ',x,'>',y,x>y)
		elif(b==2):
			x = int(input('end the value of x'))
			y = int(input('end the value of y'))
			print ('\n' * 50)	
			if (x < y):
				print('x Less that y ',x,'<',y,x<y)
			else:
				print('x not Less then y ',x,'<',y,x<y)
		elif(b==3):
			x = int(input('end the value of x'))
			y = int(input('end the value of y'))
			print ('\n' * 50)	
			if (x == y):
				print('x Equal to y ',x,'=',y,x==y)
			else:
				print('x not Equal to y ',x,'=',y,x==y)
		elif(b==4):
			x = int(input('end the value of x'))
			y = int(input('end the value of y'))
			print ('\n' * 50)	
			if (x == y):
				print('x is Not equal y',x,'!=',y,x!=y)
			else:	
				print('x Equal to y ',x,'=',y,x!=y)
		else:
			b=0

	elif(a==3):
		print ('\n' * 50)
		print ('--> Logical operators')
		print ('and	True if both the operands are true	x and y')
		print ('or	True if either of the operands is true	x or y')
		print ('not	True if operand is false (complements the operand)	not x')
		x = True
		y = False
		print('x = True  y = False')
		# Output: x and y is False
		print('x and y is',x and y)
		# Output: x or y is True
		print('x or y is',x or y)
		# Output: not x is False
		print('not x is',not x)
		print(bin(3))

	elif(a==4):
		print ('\n' * 50)
		print ('                 --> Bitwise operators')
		print ('1 -> &	Bitwise AND	')
		print ('2 -> |	Bitwise OR	x | y	')
		print ('3 -> ~	Bitwise NOT	~x 	')
		print ('4 -> ^	Bitwise XOR	x ^ y	')
		print ('5 -> >>	Bitwise right shift	x>> 	')
		print ('6 -> <<	Bitwise left shift	x<< ')
		print ('0 -> Exit')
		b = int(input('                 ---> Please enter a number <--'))

	elif(a==5):
		print ('\n' * 50)
		print ('                 --> Assignment operators')
		# Operator	Example	Equivatent to
		print ('1 -> Operator =')
		print ('2 -> Operator +=')
		print ('3 -> Operator -=')
		print ('4 -> Operator *=')
		print ('5 -> Operator /=')
		print ('6 -> Operator %=')
		print ('7 -> Operator //=')
		print ('8 -> Operator **=')
		print ('9 -> Operator &=')
		print ('10 -> Operator |=')
		print ('11 -> Operator ^=')
		print ('12 -> Operator >>=')
		print ('13 -> Operator <<=')
		b = int(input('                 ---> Please enter a number for operator <--'))
		x = int(input('                 ---> Please enter a number for x =  <--'))
		Assop(b,x)

	elif(a==6):
		print ('\n' * 50)
		print ('                 --> Identity operators')
		print ('Example : a1 = 5, b1 = 5,a2 = ''''Hello'''',b2 = ''''Hello'''',a3 = [1,2,3],b3 = [1,2,3]')
		a1 = 5
		b1 = 5
		a2 = 'Hello'
		b2 = 'Hello'
		a3 = [1,2,3]
		b3 = [1,2,3]
		# Output: False
		print('a1 is not b1  >  ',a1 is not b1)
		# Output: True
		print('a2 is b2  >', a2 is b2)
		# Output: False
		print('a3 is b3',a3 is b3)
		print('\n\n\n')
		# b = int(input('                 ---> Please enter a number <--'))
	elif(a==7):
		print ('\n' * 50)
		print ('                 --> Membership operators')
		# b = int(input('                 ---> Pleas?e enter a number <--'))
		print(' 		x = ''Hello world''		y = {1:''a'',2:''b''}')
		x = 'Hello world'		
		y = {1:'a',2:'b'}
		# Output: True
		print('H in x','H' in x)
		# Output: True
		print('hello not in x', 'hello' not in x)
		# Output: True
		print('1 in y', 1 in y)
		# Output: False
		print('a in y', 'a' in y)
		print('\n\n\n')
	elif(a==0):
		a=0
	else:
		print ('\n' * 50)
		print('input is incorrect\n')

# if a in [1,2,3,4,5,6,7]:
# 	print (a)
# else:
# 	print ('invalid number entered')
# #'1 -> Arithmetic operators'
# #'2 -> Comparison operators'
# #'3 -> Logical operators'
# #'4 -> Bitwise operators'
# #'5 -> Assignment operators'
# #'6 -> Identity operators'
# #'7 -> Membership operators'

