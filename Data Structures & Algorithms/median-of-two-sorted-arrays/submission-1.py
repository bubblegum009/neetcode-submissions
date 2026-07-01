class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        low=0
        n=len(nums)
        if(n%2!=0):
            return nums[n//2]
        else:
            return ( nums[(n-1)//2]+nums[(n+1)//2])/2