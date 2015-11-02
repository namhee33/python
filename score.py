def score_to_grade(score):
	grade = ''
	if score < 60:
		print 'The score must be between 60 and 100!'
	elif 60 <= score and score <= 69:
		grade = 'D'
	elif 70 <= score and score <= 79:
		grade = 'C'
	elif 80 <= score and score <= 89:
		grade = 'B'
	elif 90 <= score and score <= 100:
		grade = 'A'
	else: 
		print 'The score must be between 60 and 100!'
	if grade != '':
		return grade

print("Scores and Grades")
for i in range(0,10):
	print('score: {0} Your grade is'.format(raw_input())),	
print 'End of the program. Bye!'
