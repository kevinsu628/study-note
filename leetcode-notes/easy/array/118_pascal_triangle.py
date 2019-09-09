'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # init
        tri = [[1]*(i+1) for i in range(numRows)]

        if numRows <= 2:
        	return tri

        for i in range(2,len(tri)):
        	prev_row = tri[i-1]
        	row = tri[i]

        	for j in range(1,len(row)-1):
        		row[j] = prev_row[j-1] + prev_row[j]

        return tri
