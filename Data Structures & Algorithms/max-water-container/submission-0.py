class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxv=0
        while(i<j):
            curv=(j-i)*min(heights[i],heights[j])
            maxv=max(maxv,curv)
            if(heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        return maxv
