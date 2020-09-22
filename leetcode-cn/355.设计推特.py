#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
from typing import List
from collections import defaultdict


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.post = []
        self.follows = defaultdict(list)
        self.post_user = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.post.append(tweetId)
        self.post_user[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = []
        for p in self.post[::-1]:
            if self.post_user[p] in self.follows[userId] or self.post_user[
                    p] == userId:
                feed.append(p)
                if len(feed) == 10:
                    break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
