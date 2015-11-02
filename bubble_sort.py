
x = [13,1,5,6,2,4,7,0]
last_index = len(x)-1
for i in range(0, last_index):
	for j in range(0, last_index-i):
		if x[j] > x[j+1]:
			temp = x[j]
			x[j] = x[j+1]
			x[j+1] = temp
		print i, x
print 'sorted x: ' + str(x)
