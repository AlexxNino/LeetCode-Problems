from typing import List
A = [1,2]
B = [-2,-1]
C = [-1,2]
D = [0,2]
binary = []

def Decimal2Binary(n:int):
	j = len(binary)
	for k in range(j):
		binary.pop(0)
	while n > 0:
		remainder = n % 2
		n = int(n / 2)
		binary.append(remainder)
	while len(binary) < 4:
		binary.append(0)
	binary.reverse()



def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
	counter = 0
	for i in range(15):
		Decimal2Binary(i)
		if A[binary[0]]+B[binary[1]]+C[binary[2]]+D[binary[3]] == 0:
			counter += 1
	print(binary , A[binary[0]]+B[binary[1]]+C[binary[2]]+D[binary[3]])
	print(counter)
	return counter


fourSumCount(None,A,B,C,D)
