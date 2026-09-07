class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        box=defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                ch=board[i][j]
                if ch!=".":
                    if ch in rows[i] or ch in cols[j] or ch in box[(i//3,j//3)] :
                        return False
                    rows[i].add(ch)
                    cols[j].add(ch)
                    box[(i//3,j//3)].add(ch)

        return True
