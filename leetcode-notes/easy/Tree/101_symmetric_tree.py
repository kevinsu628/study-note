'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''

'''
Approach 1: recursion
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (node1.val == node2.val) \
                and isMirror(node1.left, node2.right) \
                and isMirror(node1.right, node2.left) 
        
        return isMirror(root, root)


'''
appraoch 2: interative
'''

from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            else:
                return True
            
        deq = deque([(root, root),])
        
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if q:
                deq.append((p.left, q.right))
                deq.append((p.right, q.left))
                
        return True
            
            
        
        
    









