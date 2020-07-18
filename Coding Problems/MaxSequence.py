given = [5,2,99,3,4,1,100]

def maxSeq(given):
	given.sort()
	highest = 1
	temp = 1
	for i in range(1,len(given)):
		last = given[i-1]
		current = given[i]
		if (current - last) == 1:
			temp+=1
		else:
			if temp > highest:
				highest = temp
			temp = 0
	return highest
