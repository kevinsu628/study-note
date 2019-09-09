'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two 
adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
'''

'''
have two dp memory: startFromFirstHouse, startFromSecondHouse
startFromFirstHouse: consider robing the 1st house of not. 
	Initialized list: [num[0], max(num[0], num[1])]
startFromSecondHouse: don't consider the 1st house 
	Initialized list: [0, num[1]]

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
        
        startFromFirstHouse_dp = [num[0], max(num[0], num[1])]
        startFromSecondHouse_dp = [0, nums[1]]

        for i in range(2, len(nums)-1):
            startFromFirstHouse_dp.append(max(startFromFirstHouse_dp[i-2]+nums[i], startFromFirstHouse_dp[i-1]))
        for i in range(2, len(nums)):
            startFromSecondHouse_dp.append(max(startFromSecondHouse_dp[i-2]+nums[i], startFromSecondHouse_dp[i-1]))

        return max(startFromFirstHouse_dp[-1], startFromSecondHouse_dp[-1])