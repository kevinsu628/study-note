'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).


#https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image

 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
'''
class Solution(object):
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]


'''
The most pythonic solution is a simple one-liner using [::-1] to flip the matrix upside down and then zip to transpose it. 
It assigns the result back into A, so it's "in-place" in a sense and the OJ accepts it as such, though some people might not.

'''
    def rotate(self, A):
        A[:] = zip(*A[::-1])

'''
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7

void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

'''