'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: 
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left == None:
            return
        
        node = root.left
        while node.right:
            node = node.right
        
        node.right = root.right
        root.right = root.left
        root.left = None
        
        return 
            