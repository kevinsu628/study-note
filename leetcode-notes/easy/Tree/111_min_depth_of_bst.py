'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(node):
            if not node:
                return 0
            else:
                min_left_depth = getDepth(node.left)
                min_right_depth = getDepth(node.right)
                if min_left_depth == 0 or min_right_depth == 0:
                    return 1 + min_left_depth + min_right_depth
                else:
                    return 1 + min(min_left_depth, min_right_depth)
        return getDepth(root)