class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for i in range(0,len(nums)):
            freq_map[nums[i]]=1+freq_map.get(nums[i],0)

        #Initilaise a heap 
        heap=[]
        #Iterate through the hashmap
        for num,freq in freq_map.items():
            heapq.heappush(heap,(freq,num))

            if(len(heap)>k):
                heapq.heappop(heap)

        return [num for freq,num in heap]