class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        #Set initial time as 0
        time=0
        q=deque()

        while maxHeap or q:
            time+=1

            if not maxHeap:
                time=q[0][1]

            else:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    #If more execytion of task A are left put it in q
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time