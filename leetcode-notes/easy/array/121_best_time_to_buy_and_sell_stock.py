
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Straight forward:
	keep note of the min price
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        min_price = sys.maxint
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price > min_price and (price - min_price) > max_profit:
                max_profit = price - min_price
        return max_profit

'''
 but if the interviewer twists the question slightly by giving the difference array of prices, 
 Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.

 This becomes find maxSubArray problem
'''

def maxProfit(prices):
    maxCur = 0, 
    maxSoFar = 0;
    for i in range(1, len(prices)):
    	maxCur += (prices[i] - prices[i-1])
        maxCur = Math.max(0, maxCur)

        maxSoFar = Math.max(maxCur, maxSoFar)

    return maxSoFar;
    