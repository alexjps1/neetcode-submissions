class Solution:
    def fill(self, row, col, grid):
        stack = [(row, col)]
        while len(stack) > 0:
            row, col = stack.pop()
            grid[row][col] = "2"

            d = (min(row+1, len(grid)-1), col)
            u = (max(row-1, 0), col)
            l = (row, max(col-1, 0))
            r = (row, min(col+1, len(grid[0])-1))

            for i in [u, d, l, r]:
                if grid[i[0]][i[1]] == "1":
                    stack.append(i)


    def numIslands(self, grid: List[List[str]]) -> int:
        i = 0
        j = 0
        n_islands = 0
        while i < len(grid):
            while j < len(grid[0]):
                if grid[i][j] == "1":
                    self.fill(i, j, grid)
                    n_islands += 1
                j += 1
            j = 0
            i += 1
    
        return n_islands
            
    