'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''

Sliding window:
create a longest window that contains a unique substring. 
extend the rigth side of window one char by one char and check validation
If running duplicate, move left index to the right by 1. 
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        w_dict = {}
        i = 0
        j = 0
        
        while i < n and j < n:
            # first: extend range
            if not s[j] in w_dict:
                w_dict[s[j]] = 1
                j+=1
                max_len = max(j-i, max_len)
            else:
                w_dict.pop(s[i])
                i+=1
        return max_len


'''
Optimized sliding window 
Jump straight to the position when duplicated char is detected
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        w_dict = {} # char : index
        i = 0
        j = 0
        
        while j < n:
            if s[j] in w_dict:
                # the left index can jump directly to the next position of the duplicated character 
                i = max(i, w_dict[s[j]])
                
            # no matter if it exists or not, we update the char in the set to be the 
            # latest position 
            max_len = max(max_len, j-i+1)
            # put it to the next position to can jump straight to it
            w_dict[s[j]] = j+1
            
            j += 1
            
        return max_len










