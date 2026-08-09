class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(9): # row
            for j in range(9): # col
                val = board[i][j]
                if val == '.':
                    continue
                k = 3 * (i//3) + j//3 #square
                print(i, j, k)
                bit = 1 << (int(val) - 1)
                if (rows[i] | cols[j] | squares[k]) & bit > 0:
                    return False
                rows[i] |= bit
                cols[j] |= bit
                squares[k] |= bit

        return True 

