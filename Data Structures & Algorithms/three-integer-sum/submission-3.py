class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        results=[]
        for i in range(0,len(nums)-2):
            if(i>0 and nums[i-1]==nums[i]):
                continue
            j=i+1
            k=len(nums)-1
            while(j<k and j<len(nums)):
                threesum=nums[i]+nums[j]+nums[k]
                if(threesum==0):
                    results.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                elif(threesum < 0):
                    j+=1
                else:
                    k-=1
        return results

