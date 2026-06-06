class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = defaultdict(list)
        self.followers_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.user_tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        users = set(self.followers_map[userId])
        users.add(userId)
        
        for u_id in users:
            if u_id in self.user_tweets:
                tweets = self.user_tweets[u_id]
                index = len(tweets) - 1
                if index >= 0:
                    time, t_id = tweets[index]
                    min_heap.append((-time, t_id, u_id, index - 1))
                    
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            neg_time, t_id, u_id, nxt_idx = heapq.heappop(min_heap)
            res.append(t_id)
            if nxt_idx >= 0:
                nxt_time, nxt_tid = self.user_tweets[u_id][nxt_idx]
                heapq.heappush(min_heap, (-nxt_time, nxt_tid, u_id, nxt_idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers_map[followerId]:
            self.followers_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)