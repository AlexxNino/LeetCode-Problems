stringer = "-2342"

def StringToInt():
	integer = 0
	maxLen = len(stringer)
	if stringer[0] == "-":
		for i in range(maxLen-1):
			integer -= int(stringer[maxLen-(1+i)]) * (10**i)
	else:
		for i in range(maxLen):
			integer += int(stringer[maxLen-(1+i)]) * (10**i)
	return integer

print(StringToInt())
