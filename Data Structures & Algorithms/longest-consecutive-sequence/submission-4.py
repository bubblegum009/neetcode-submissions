class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
       
        longest=1
        for num in nums:
            if num-1 not in nums:
                long=1
                while(num+1 in nums):
                    long+=1
                    num=num+1
                longest=max(long,longest)

        return longest