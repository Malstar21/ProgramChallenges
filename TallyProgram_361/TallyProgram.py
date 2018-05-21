dict = {'A' : 0,
		'B' : 0,
		'C' : 0,
		'D' : 0,
		'E' : 0}

score = input('Enter scores:')
#print(score)

for x in score:
	if x.islower():
		#Add point to player x
		dict[x.upper()] += 1
	elif x.isupper():
		#Subtract point from player x
		dict[x] -= 1

scores = sorted(dict.items(), key = lambda t:t[1], reverse=True)

for key,val in scores:
	print(key,":", val)