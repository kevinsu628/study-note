'''
Question:
	Given a sorted array nums, remove the duplicates in-place such that each element appear 
	only once and return the new length.

	Do not allocate extra space for another array, 
	you must do this by modifying the input array in-place with O(1) extra memory.

Approach 1: Two Pointers
Algorithm

Since the array is already sorted, we can keep two pointers i and j, where i is the slow-runner while j is the fast-runner. 
As long as nums[i] = nums[j], we increment j to skip the duplicate.

When we encounter nums[j] != nums[i]
the duplicate run has ended so we must copy its value to nums[i + 1]
i is then incremented and we repeat the same process again until j reaches the end of array.
'''

def removeDuplicate(nums):
	for i in range(len(nums)):
		for j in range(1, len(nums)):
			if nums[i] != nums[j]:
				i += 1
				nums[i] = nums[j]