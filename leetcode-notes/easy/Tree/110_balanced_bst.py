'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

'''
Approach 1: recursion (bad) Run time: O(N^2)
'''

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def recursion(root):
            if not root:
                return 0
            else:
                left_depth = recursion(root.left)
                right_depth = recursion(root.right)
                return 1 + max(left_depth, right_depth)
            
        if not root:
            return True
        else:
            return math.fabs(recursion(root.left) - recursion(root.right)) <= 1 \
                   and self.isBalanced(root.left) and self.isBalanced(root.right)


'''
Approach 1: recursion (bad) Run time: O(N^2)
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfsHeight(node):
            if not node:
                return 0
            
            
            left_depth = dfsHeight(node.left)
            if left_depth == -1:
                return -1
            right_depth = dfsHeight(node.right)
            if right_depth == -1:
                return -1

            if math.fabs(left_depth - right_depth) > 1:
                return -1
                
            return 1 + max(left_depth, right_depth)
            
        return dfsHeight(root) != -1



