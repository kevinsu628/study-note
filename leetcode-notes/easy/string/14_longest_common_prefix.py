'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
'''

'''
Approach 1: horizontal scanning

func(input) = common(common(flower, flow), flight) = fl
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

       	if len(strs) == 0:
       		return ""

       	pref = strs[0]

       	for word in strs:
       		while strs[i].find(pref) != 0:
       			pref = pref[:-1]
       			if len(pref) == 0:
       				return ""
       	return pref


'''
vertical scanning:
if there is a very small string at the end of array
will be inefficient.
Sol: check the char at index i for each word. return the pref if one of them is not consistent any more
'''
class Solution(object):
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        for i, c in enumerate(strs[0]):
            for other_word in strs[1:]:
                if i >= len(other_word) or other_word[i] != c:
                    return strs[0][:i]

        return strs[0]