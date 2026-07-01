class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        cur=[]
        def dfs(openp,closep):
            if openp==closep==n:
                result.append("".join(cur))
                return

            if openp < n:
                cur.append("(")
                dfs(openp+1,closep)
                cur.pop()
            if closep < openp:
                cur.append(")")
                dfs(openp,closep+1)
                cur.pop()

            

        dfs(0,0)
        return result