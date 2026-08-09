class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_set(l: list):
            nums = [item for item in l if item != '.']
            return len(set(nums)) == len(nums)
        
        valid = True 

        # rows
        for row in board:
            valid = min(valid, valid_set(row))
            if not valid:
                print(f"invalidated at row {row}")

        
        # cols
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            valid = min(valid, valid_set(col))
            if not valid:
                print(f"invalidated at col{i}")
                print(f"col contents: {col}")

        # boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                square += board[i][j:j+3]
                square += board[i+1][j:j+3]
                square += board[i+2][j:j+3]
                valid = min(valid, valid_set(square))
                if not valid:
                    print(f"invalidated at square {i},{j}")
                    print("square contents: ", square)

        return valid


