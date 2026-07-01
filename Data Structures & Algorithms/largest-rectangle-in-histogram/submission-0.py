class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #Array to store left highest index
        left=[-1]*len(heights)
        #Array to store right highest index
        right=[len(heights)]*len(heights)
        st=[]
        #Right highest index
        for i in range(0,len(heights)):
            while st and heights[st[-1]]>=heights[i]:
                right[st.pop()]=i

            st.append(i)
        st=[]
        #Left highest index
        for j in range(len(heights)-1,-1,-1):
            while st and heights[st[-1]]>heights[j]:
                left[st.pop()]=j
            st.append(j)
        maxa=0
        for i in range(0,len(heights)):
            area=heights[i]*(right[i]-left[i]-1)
            if(area>maxa):
                maxa=area
        return maxa
