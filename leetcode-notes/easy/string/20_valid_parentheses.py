'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

'''

class Solution:
    def isValid(self, s):
    	p_dict = {
    		"]": "[",
    		"}": "{",
    		")": "("
    	}

    	stack = []

    	for c in s:
    		if c in p_dict.values():
    			stack.append(c)

    		elif c in p_dict.keys():
    			if len(stack) == 0 or p_dict[c] != stack.pop():
    				return False
    		else: 
    			return False
    	return len(stack) == 0
