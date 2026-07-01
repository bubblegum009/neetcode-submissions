class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res=[]
        p=[]

        def part(i):
            if i==len(s):
                res.append(p.copy())
                return
            
            for j in range(i,len(s)):
                if self.ispali(s,i,j):
                    p.append(s[i:j+1])
                    part(j+1)
                    p.pop()

        part(0)
        return res

    def ispali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True