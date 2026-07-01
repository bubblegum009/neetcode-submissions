class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]
        nums.sort()

        def findsubset(start):
            if start==len(nums):
                result.append(subset[:])
                return

    
            subset.append(nums[start])
            findsubset(start+1)
            subset.pop()
            while start+1<len(nums) and nums[start]==nums[start+1]:
                start=start+1
            findsubset(start+1)

        findsubset(0)
        return result