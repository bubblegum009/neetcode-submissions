class MedianFinder:

    def __init__(self):
        #For right half of the array
        self.minheap=[]
        #For left half of the array
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        if self.minheap and num>self.minheap[0]:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush(self.maxheap,-num)

        #Balanc ethe heaps when length diff is more than 1
        if len(self.minheap)>len(self.maxheap)+1:
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))
        
        if len(self.maxheap)>len(self.minheap)+1:
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
    def findMedian(self) -> float:

        if len(self.minheap)>len(self.maxheap):
            return self.minheap[0]

        
        elif len(self.minheap)<len(self.maxheap):
            return -self.maxheap[0]

        else:
            return (self.minheap[0]-self.maxheap[0])/2.0
        
        
        