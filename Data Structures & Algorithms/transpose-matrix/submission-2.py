class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        t = [[None] * n for i in range(m)]
        print(len(t), len(t[0]))
        for i in range(m):
            for j in range(n):
                t[i][j] = matrix[j][i]
        return t
