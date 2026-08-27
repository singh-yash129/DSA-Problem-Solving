class Twitter:

    def __init__(self):
        self.tweetFeed = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetFeed:
            self.tweetFeed[userId] = {
                "tweetID": [],
                "followerID": [],
                "followeeID": []
            }
        self.tweetFeed[userId]["tweetID"].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list:
        all_tweets = []
        
        if userId in self.tweetFeed:
            all_tweets.extend(self.tweetFeed[userId]["tweetID"])
            for followeeId in self.tweetFeed[userId]["followeeID"]:
                if followeeId in self.tweetFeed:
                    all_tweets.extend(self.tweetFeed[followeeId]["tweetID"])

        all_tweets.sort(key=lambda x: x[0], reverse=True)
        return [tweetId for _, tweetId in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.tweetFeed:
            self.tweetFeed[followerId] = {
                "tweetID": [],
                "followerID": [],
                "followeeID": []
            }
        if followeeId not in self.tweetFeed[followerId]["followeeID"]:
            self.tweetFeed[followerId]["followeeID"].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.tweetFeed:
            if followeeId in self.tweetFeed[followerId]["followeeID"]:
                self.tweetFeed[followerId]["followeeID"].remove(followeeId)