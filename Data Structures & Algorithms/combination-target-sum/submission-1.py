class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def dfssum(start,totsum):
            if totsum==target:
                res.append(cur[:])
                return

            for i in range(start,len(nums)):
                if(totsum+nums[i])>target:
                    return
                cur.append(nums[i])
                dfssum(i,totsum+nums[i])
                cur.pop()

        res=[]
        cur=[]
        dfssum(0,0)
        return res