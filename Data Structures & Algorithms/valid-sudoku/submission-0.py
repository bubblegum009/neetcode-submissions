class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map=defaultdict(list)
        col_map=defaultdict(list)
        sq_map=defaultdict(list)

        #Check duplicate in a row
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col]==".":
                    continue
                if (board[row][col] in row_map[row] or
                board[row][col] in col_map[col] or 
                board[row][col] in sq_map[(row//3,col//3)]):
                    return False

                #Add to row
                row_map[row].append(board[row][col])
                col_map[col].append(board[row][col])
                sq_map[(row//3,col//3)].append(board[row][col])

        return True


      