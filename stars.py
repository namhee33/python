import sys
def draw_stars(x):
	for i in x:
		for star_count in range(0,i):
			sys.stdout.write('*')
		print

def draw_letters(x):
	for data in x:
		if not isinstance(data, int):
			count = len(data)
			first_letter = data[0].lower()
			star = False
		else:
			count = data
			star = True
		for star_count in range(0,count):
			if(star):
				sys.stdout.write('*')
			else:
				sys.stdout.write(first_letter)
		print

x = [4,6,1,3,5,7,25]
y = [4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy Smith']

draw_stars(x)
print 'Drawing stars end..... Press Enter key to continue...'
raw_input()
draw_letters(y)



