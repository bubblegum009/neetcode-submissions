class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for i in range(0,len(nums)):
            freq_map[nums[i]]=1+freq_map.get(nums[i],0)

        #Initilaise a array for bucket sort
        count=[[] for i in range(len(nums)+1)]
        #Iterate through the hashmap
        for num,freq in freq_map.items():
            #Append numbers againt frequncy on count array
            count[freq].append(num)
        result=[]
        #Iterate through count
        for i in range(len(count)-1,0,-1):
            for num in count[i]:
                result.append(num)
                if(len(result)==k):
                    return result
