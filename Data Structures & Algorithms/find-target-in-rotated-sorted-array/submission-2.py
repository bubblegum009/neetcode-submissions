class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                return mid
            #Find which sorted half has the target
            #If number at low is less tahn number at mid then left half is sorted
            elif(nums[low]<=nums[mid]):
                if(nums[low]<=target<nums[mid]):
                    high=mid-1
                else:
                    low=mid+1
            else:
                if(nums[mid]<target<=nums[high]):
                    low=mid+1
                else:
                    high=mid-1
        return -1
            
