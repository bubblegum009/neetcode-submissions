class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash={}
        for i in range(0,len(nums)):
            if(target-nums[i] in sum_hash):
                return [sum_hash[target-nums[i]],i]
            sum_hash[nums[i]]=i
        return []    