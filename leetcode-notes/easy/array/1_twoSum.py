'''
Question: 
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	

Approach 1: Brute Force
	The brute force approach is simple. Loop through each element xx and find 
	if there is another value that equals to target - xtarget−x.

'''
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
            	return [nums[i], nums[j]]
            
    print("no two sum")

'''
Approach 3: One-pass Hash Table
	It turns out we can do it in one-pass. 
	While we iterate and inserting elements into the table, 
	we also look back to check if current element's complement already exists in the table. 
	If it exists, we have found a solution and return immediately.
'''

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


print(twoSum([2, 7, 11, 15], 9))
