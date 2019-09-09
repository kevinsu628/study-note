'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Approach 1: 
reverse 3 times

[1,2,3,4,5,6,7]
[7,6,5,4,3,2,1]
[5,6,7,4,3,2,1]
[5,6,7,1,2,3,4]
'''


class Solution:
    def rotate(self, nums, k):
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)
            
            
'''
approach 2:
copy to another array
'''
    def rotate(self, nums, k):
        a = [1] * len(nums)
        for i in range(len(nums)):
            a[(i + k) % nums.length] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = a[i]
