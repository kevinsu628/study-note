'''
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

'''
Aspprach 1: brute force
1. Traverse all the linked lists and collect the values of the nodes into an array.
2. Sort and iterate over this array to get the proper value of nodes.
3. Create a new sorted linked list and extend it with the new nodes.
'''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


'''
Time: O(Nlog N)

Collecting all the values costs O(N) time.
A stable sorting algorithm costs O(NlogN) time.
Iterating for creating the linked list costs O(N)

Space: O(N).
Sorting cost O(N) space (depends on the algorithm you choose).
Creating a new linked list costs O(N) space.
'''

'''
Approach 2: Compare 1 by 1 + priority queue
'''
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
'''
Time: 
Without priority list, O(kn)
With priority list, O(nlogk)
	Note: The comparison cost will be reduced to O(logk) for every pop and insertion 
	to priority queue. But finding the node with the smallest value just costs O(1) time.
	There are n nodes in the final linked list.

Space: 
Without priority list, O(n)
With priority list, O(n)
'''

'''
Approach 3: divide and conquer 
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next














