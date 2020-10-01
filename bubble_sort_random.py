
import random
x=[]
for i in range(0,100):
	random_num = random.random()
	random_num *= random_num * 10000 
	random_num = int(random_num)
	x.append(random_num)

print ('Unsorted X')
for i in range(0,10):
	for j in range(0,10):
		print '{0:5d}'.format(x[j+i*10])
last_index = len(x)-1
for i in range(0, last_index):
	for j in range(0, last_index-i):
		if x[j] > x[j+1]:
			temp = x[j]
			x[j] = x[j+1]
			x[j+1] = temp

print ('Sorted x')		
for i in range(0,10):
	for j in range(0,10):
		print '{0:5d}'.format(x[j+i*10])
