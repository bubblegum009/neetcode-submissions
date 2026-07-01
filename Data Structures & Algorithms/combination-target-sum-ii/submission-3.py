class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfssum(start,totsum):
            if totsum==target:
                res.append(cur[:])
                return
     
            for i in range(start,len(candidates)):
                if(totsum+candidates[i])>target :
                    return
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                cur.append(candidates[i])
           
                dfssum(i+1,totsum+candidates[i])
                cur.pop()

        res=[]
        cur=[]
        candidates.sort()
        dfssum(0,0)
        return res