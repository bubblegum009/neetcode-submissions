class TimeMap:

    def __init__(self):
        self.timemap=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr=self.timemap.get(key,[])
        if not arr:
            return ""
        res=""
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            val=arr[mid][1]
            if(val<=timestamp):
                res=arr[mid][0]
                low=mid+1
            else:
                high=mid-1
        return res
                
        
