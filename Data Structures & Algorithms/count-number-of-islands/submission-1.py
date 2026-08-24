class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        seen = set()
        ct = 0

        def dfs(root: Tuple[int, int]) -> None:
            stack = [root]
            while stack:
                cur = stack.pop()
                seen.add(cur)
                i, j = cur
                # up
                if i > 0 and grid[i-1][j] == "1" and (i-1, j) not in seen:
                    stack.append((i-1, j))
                # down
                if i < n-1 and grid[i+1][j] == "1" and (i+1, j) not in seen:
                    stack.append((i+1, j))
                # left
                if j > 0 and grid[i][j-1] == "1" and (i, j-1) not in seen:
                    stack.append((i, j-1))
                # right
                if j < m-1 and grid[i][j+1] == "1" and (i, j+1) not in seen:
                    stack.append((i, j+1))


        for i in range(n):
            for j in range(m):
                if (i, j) not in seen and grid[i][j] == "1":
                    dfs((i, j))
                    ct += 1
        
        return ct