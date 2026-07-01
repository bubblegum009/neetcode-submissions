class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=height[0]
        right_max=height[right]
        vol=0
        while(left<right):
            if(left_max<right_max):
                left=left+1
                left_max=max(left_max,height[left])
                vol=vol+left_max-height[left]
            else:
                right=right-1
                right_max=max(right_max,height[right])
                vol=vol+right_max-height[right]

        return vol