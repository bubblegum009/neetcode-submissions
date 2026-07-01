class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(0,len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                tsum=nums[i]+nums[j]+nums[k]
                if(tsum>0):
                    k=k-1
                elif(tsum<0):
                    j=j+1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    while(j<k and nums[j]==nums[j-1]):
                        j=j+1

        return res

