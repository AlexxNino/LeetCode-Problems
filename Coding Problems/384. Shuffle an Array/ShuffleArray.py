
import random

nums = [1,2,3]

class test(object):
	def __init__(self,nums):
		self.nums = nums
	def reset(self):
		return self.nums
	def shuffle(self):
		CopyList = self.nums[:]
		random.shuffle(CopyList)
		return CopyList

obj = test(nums)

test2 = obj.shuffle()
print(test2)

test3 = obj.reset()
print(test3)