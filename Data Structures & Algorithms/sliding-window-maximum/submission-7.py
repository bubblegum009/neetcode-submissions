class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        heap=[]
        right=0
        result=[]

        left=0
        for right in range(0,len(nums)):
            heapq.heappush(heap,(-nums[right],right))
            if(right-left+1==k):
                num=heap[0][0]
                pos=heap[0][1]
                while(pos<left):
                    heapq.heappop(heap)
                    num=heap[0][0]
                    pos=heap[0][1]
                result.append(-num)
                left+=1
        return result