class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stones in stones:
            heapq.heappush(heap,-stones)

        while(len(heap)>1):
            stone1=-heapq.heappop(heap)
            stone2=-heapq.heappop(heap)
            if(stone1>stone2):
                heapq.heappush(heap,-(stone1-stone2))

        return -heapq.heappop(heap) if heap else 0
