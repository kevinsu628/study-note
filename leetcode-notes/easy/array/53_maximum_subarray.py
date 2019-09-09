'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

'''
Intuition: 

At first, I think the sub problem should look like: maxSubArray(int A[], int i, int j), 
which means the maxSubArray for A[i: j]. In this way, our goal is to figure out 
what maxSubArray(A, 0, A.length - 1) is. However, if we define the format of the sub 
problem in this way, it's hard to find the connection from the sub problem to the 
original problem(at least for me). In other words, I can't find a way to divided 
the original problem into the sub problems and use the solutions of the sub problems
to somehow create the solution of the original one.

So I change the format of the sub problem into something like: 
maxSubArray(int A[], int i), which means the maxSubArray for A[0:i ] 
which must has A[i] as the end element. Note that now the sub problem's format 
is less flexible and less powerful than the previous one because 
there's a limitation that A[i] should be contained in that sequence and 
we have to keep track of each solution of the sub problem to update the 
global optimal value. However, now the connect between the sub problem & 
the original one becomes clearer:

maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]; 


'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
        	return 0

        dp = {
        	0: nums[0]
        } 

        max_sofar = dp[0]
        
        for i in list(range(1,n)):
        	# get the previous largest subarray's sum
            prev = dp[i-1] if dp[i-1] > 0 else 0
            # the maximum sum that contains nums[i]
            dp[i] = max(nums[i], prev+nums[i])
            # get the maximum 
            max_sofar = max(max_sofar, dp[i])
            
        return max_sofar






