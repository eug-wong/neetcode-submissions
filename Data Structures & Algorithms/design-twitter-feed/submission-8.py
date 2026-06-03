from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        # hashamp to keep track of followers
        # for each follower, we can get the list using hashmap
        # push tweetIds onto heap and then pop off the top 10 ---> minheap adn just pop until 10 remaining, and return those
        # hashmap to keep track of twwets
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        heapq.heapify(h)
        followed = self.following[userId]
        followed.add(userId)
        for f in followed:
            for p in self.tweets[f]:
                heapq.heappush(h, [p[0], p[1]])

        res = []
        while len(h) > 10:
            heapq.heappop(h)
        
        while h:
            res.append(heapq.heappop(h)[1])
        
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
