class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.time , tweetId])
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users_to_check = {userId} | self.following.get(userId , set())


        for uid in users_to_check:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time , tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx))

        result = []
        while heap and len(result) < 10:
            negTime , tweetId , uid , idx = heapq.heappop(heap)
            result.append(tweetId)

            if idx > 0:
                time, tweetId2 = self.tweets[uid][idx - 1]
                heapq.heappush(heap , (-time, tweetId2 , uid , idx - 1))


        
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


