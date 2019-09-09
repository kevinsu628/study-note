'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        
        if not root:
            return ret
        
        stack = [(root, 0)]
        
        while len(stack) != 0:
            node, level = stack.pop()
            if not node:
                continue
                
            while(len(ret) < level+1):
                ret.append([])
            
            if level%2 == 0:
                ret[level].insert(0, node.val)
            else:
                ret[level].append(node.val)
                
            stack.append((node.left, level+1))
            stack.append((node.right, level+1))
        return ret


        