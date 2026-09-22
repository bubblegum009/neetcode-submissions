class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        results=[0]*n
        st=[]
        for i in range(0,n):
            while st and st[-1][1]< temperatures[i]:
                results[st[-1][0]]=i-st[-1][0]
                st.pop()
            st.append((i,temperatures[i]))

        return results