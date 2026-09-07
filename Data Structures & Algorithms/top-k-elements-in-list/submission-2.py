class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap=[]
        count_map={}

        for i in range(0,len(nums)):
            count_map[nums[i]]=count_map.get(nums[i],0)+1

        for key,value in count_map.items():
            heapq.heappush(minheap,(value,key))

            if(len(minheap)>k):
                heapq.heappop(minheap)

        return [val for key,val in minheap]
