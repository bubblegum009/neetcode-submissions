class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)

        for i in range(0,len(nums)-1):
            ans[i+1]=ans[i]*nums[i]
        right=1
        for i in range(len(nums)-2,-2,-1):
            ans[i+1]=ans[i+1]*right
            right=right*nums[i+1]

        return ans
