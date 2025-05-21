from collections import deque
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        rs=set()
        cs=set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rs.add(i)
                    cs.add(j)

        for i in range(r):
            for j in range(c):
                if i in rs or j in cs:
                    matrix[i][j]=0
        return matrix



