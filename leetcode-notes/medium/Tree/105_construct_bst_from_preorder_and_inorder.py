'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Intuition: 
inorder: left root right
preorder: root left right 
postorder: left right root 
1. pop the root of preorder. 
2. find the index of the root in the inorder 
3. Then everything in [:idx] of inorder is in the left, otherwise on the right of the root 
4. note: the order you call recursion should be the same as the order you choose to pop up node (in this case: preorder)
'''

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            val = preorder.pop(0)
            in_position = inorder.index(val)
            node = TreeNode(val)
            node.left = self.buildTree(preorder, inorder[:in_position])
            node.right = self.buildTree(preorder, inorder[in_position+1:])
            return node 