'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None 
        curr = head 
        while curr != None:
        	nextTemp = curr.next
        	curr.next = prev
        	prev = curr
        	curr = nextTemp
        return prev


# Time: O(n)
# Space: O(1)


# Approach 2: Recursive 
# Assume that the rest of the list had already been reversed, 
# now how do I reverse the front part
class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
        	return head 
        p = reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        
# Time O(n). 
# Space O(n). 
# The extra space comes from implicit stack space due to recursion. 



