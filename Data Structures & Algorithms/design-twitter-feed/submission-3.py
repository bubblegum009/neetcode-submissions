class Twitter:

    def __init__(self):
        #Initialise start time
        self.time=0
        #Heap to store the tweets
        self.theap=[]
        #Hashmap to store the followers against each userid
        self.followmap=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        #Increment time
        self.time+=1
        heapq.heappush(self.theap,(-self.time,[tweetId,userId]))

    def getNewsFeed(self, userId: int) -> List[int]:
        #Iterate over the heap and add answers to the results array
        #when the userid against the tweet is in key or value dicts of hashmap
        ans=[]
        #Make a local copy of the heap
        heap=[]
        heap=self.theap.copy()
        while heap:
            time,tweets=heapq.heappop(heap)
            tweetid=tweets[1]
            tweet=tweets[0]
            if tweetid==userId or tweetid in self.followmap[userId]:
                ans.append(tweet)
            if(len(ans)==10):
                break

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followmap[followerId]:
            self.followmap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
