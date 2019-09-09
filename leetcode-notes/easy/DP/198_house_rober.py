'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.



Intution: 

n = 1: rob house[0]
n = 2: rob(max(house[0], house[1]))
n: rob(max((house[i-2] + house[i]), house[i-1]))

'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
        	return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = []
        dp.append(nums[0]) #only rob 1 house
        dp.append(max(nums[0], nums[1])) #rob 2 houses

        for i in range(2, len(nums)):
            dp.append(max(dp[i-2]+nums[i], dp[i-1]))

        return dp[len(nums)-1]