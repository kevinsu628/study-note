'''
70. Climbing Stairs
Easy

2217

81

Favorite

Share
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        
        dp = [1, 2] # 1 start has 1 comb, 2 has 2 comb
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
            
        return dp[n-1]