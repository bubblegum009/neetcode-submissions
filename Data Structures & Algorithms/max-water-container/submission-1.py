class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxheight=0
        while(i<j):
            curheight=min(heights[i],heights[j])*(j-i)
            if(heights[i]<=heights[j]):
                i+=1
            else:
                j-=1
            maxheight=max(curheight,maxheight)
        return maxheight