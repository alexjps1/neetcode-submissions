class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        if self.n == 0:
            return
        self.m = len(matrix[0])

        self.ps = [[0] * self.m for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                a = self.ps[i-1][j] if i > 0 else 0
                b = self.ps[i][j-1] if j > 0 else 0
                c = self.ps[i-1][j-1] if i > 0 and j > 0 else 0
                self.ps[i][j] = matrix[i][j] + a + b - c
        print(self.ps)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.n == 0:
            return 0
        a = self.ps[row1-1][col2] if row1 > 0 else 0
        b = self.ps[row2][col1-1] if col1 > 0 else 0
        c = self.ps[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.ps[row2][col2] - a - b + c
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)