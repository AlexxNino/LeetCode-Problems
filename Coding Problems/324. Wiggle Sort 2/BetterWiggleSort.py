#Wiggle Sort

nums = [1, 5, 1, 1, 6, 4]

nums.sort()
wiggleNums = []
for i in range((len(nums)//2)):
	wiggleNums.append(nums[i])
	wiggleNums.append(nums[len(nums)-(i+1)])
nums = wiggleNums
