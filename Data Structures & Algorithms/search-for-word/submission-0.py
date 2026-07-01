class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Get the number of rows and colums
        rows=len(board)
        col=len(board[0])
        #Set to keep the combinations of rows and cols visited
        path=set()

        #Search of character at ith position from row rand col c
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or r >= rows or c>=col or board[r][c]!=word[i] or (r,c) in path):
                return False

            path.add((r,c))
            result=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return result

        for r in range(rows):
            for c in range(col):
                if dfs(r,c,0):
                    return True

        return False