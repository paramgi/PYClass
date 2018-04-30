#formating styles
#___________________________________________________________________________________________________
#--old formating style--
a = 'superman'
b='ironman'
ad='USA'
bd='Russia'
#print ('there are two avenger named %s and %s from %s and %s respectively'%(a,b,ad,bd))
# %s ----> string
# %d ----> integer
# %f ----> float
#___________________________________________________________________________________________________
#new formating style
#.format() ---> inbuilt method
print ('there are people from {1} in the the {0} number ' .format('india',34567890))

#slicing operator on float
print ('the persentage of the {} is {:.4f}'.format('ram',9923.234567890987654))

print('lskgj{:08d}'.format(56789))

print ('{:+f} and {:-f}'.format(324.234,2345.3445))