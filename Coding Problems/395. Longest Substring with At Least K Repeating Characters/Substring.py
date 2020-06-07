def longestSubstring(self,s: str,k: int) -> int:
	CharSeen = []
	CharCount = []
	largest = 0
	for i in range(len(s)):
		if s[i] in CharSeen:
			CharSeen.count(s[i])
			CharCount[CharSeen.index(s[i])] += 1
		if s[i] not in CharSeen:
			CharSeen.append(s[i])
			CharCount.append(1)
	for j in range(len(CharCount)):
		
		if CharCount[j] >= k:
			largest += CharCount[j]
			print(CharCount[j] , largest)
	if largest < k:
		return largest
	else:
		return 0


print(longestSubstring(None,'ababacb',3))
print(longestSubstring(None,'aaabb',3))


def doStuff2(s:str):
	for c in set(s):
		print(s.count(c))
