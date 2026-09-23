class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        minh=float('inf')
        while(low<=high):
            mid=(low+high)//2
            ch=0
            for i in range(0,len(piles)):
                ch=ch+math.ceil(float(piles[i])/mid)

            if ch<=h:
                minh=min(minh,mid)
                high=mid-1
            else:
                low=mid+1
        return minh