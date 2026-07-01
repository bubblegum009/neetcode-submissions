class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(0,len(nums)-k+1):
            curr=nums[i:i+k]
            curr.sort()
            res.append(curr[-1])

        return res