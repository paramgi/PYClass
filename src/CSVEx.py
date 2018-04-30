# ----- CSV file ---

import csv

def write(fileobj,data):
	write = csv.writer(file,delimiter=',')
	for line in data:
		write.writerow(line)


def read(file)
	read = csv.dictreader(file,delimiter=',')
	print(read)
	for a in read:
		print(a['name'])
		print(a['addr'])
		print(a['phone'])

		print(70*'_')

if __name__ == '__main__':
	file = open('sample1.csv','w')
	data['name,addr,phone',split(','),
			'giri,hyd,sdf234']

write(file,data)
file=open('sample1.csv','r')
read(file)