'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

'''
Approach 1: find the longest common substring between the string and its reverse, check if the index match 
'''

'''
Approach 2: for each character, extend to the left and the right. Remember the index and the length 
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
        	return s

        idx = 0
        max_str = ""

        for i, c in enumerate(s):
        	str1 = extend(s, i, i) # if odd length
        	str2 = extend(s, i, i+1) # if even length

        	if len(str1) >= len(str2) and len(str1) > len(max_str):
        		max_str = str1
        	elif len(str2) > len(str1) and len(str2) > len(max_str):
        		max_str = str2
        		
        return max_str

def extend(s, i_, j_):
	i = i_
	j = j_

	while i >= 0 and j < len(s):
		if s[i] != s[j]:
			break
		i -= 1
		j += 1

	return s[i+1:j]

'''
Approach 3; dynamic programming

class Solution {
    public String longestPalindrome(String s) {
        if(s==null||s.length()==0) return s;
        int n=s.length();
        //substring(i,j) is panlidrome
        boolean[][] dp=new boolean[n][n];
        String res = null;
        //[j, i]
        for(int i=0;i<n;i++){
            for(int j=i;j>=0;j--){
                if(s.charAt(i)==s.charAt(j) && (i-j<2 ||dp[j+1][i-1])){
                    dp[j][i]=true;
                    if(res==null||i-j+1>res.length()){
                      res=s.substring(j,i+1);
                    }  
                }
            }
        }
        return res;
    }
}
'''











