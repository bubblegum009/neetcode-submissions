class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setarr=set(nums)
        return not len(nums)==len(setarr)