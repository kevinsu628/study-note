'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def genTreeList(start, end):
            ret = []

            if start > end:
                ret.append(None)
            
            for i in range(start, end+1):
                left_list = genTreeList(start, i-1)
                right_list = genTreeList(i+1, end)

                for each_left in left_list:
                    for each_right in right_list:
        	            new_node = TreeNode(i)
        	            new_node.left = each_left
        	            new_node.right = each_right
        	            ret.append(new_node)

            return ret
        if n == 0:
            return []
        
        return genTreeList(1, n)