'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
'''

'''
Approach 1: Peak Valley Approach
Algorithm

Say the given array is:

[7, 1, 5, 3, 6, 4].

If we analyze the graph, we notice that the points of interest are the consecutive valleys and peaks.

Total Profit= sum_{i}(height(peak_i)-height(valley_i)) 


'''
class Solution(object):
    def maxProfit(prices):
        i = 0;
        valley = prices[0];
        peak = prices[0];
        maxprofit = 0;
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i+=1
            valley = prices[i];
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i+=1
            peak = prices[i];
            maxprofit += peak - valley;
        
        return maxprofit;



'''
 go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction.
 In the end,we will be using the peaks and valleys effectively, but we need not track the costs corresponding to the peaks 
 and valleys along with the maximum profit, but we can directly keep on adding the difference between the consecutive numbers 
 of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit.

class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}

'''












