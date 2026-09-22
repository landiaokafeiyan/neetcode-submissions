import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        """
        初始化 Twitter 对象。
        
        核心数据结构：
        1. self.time: 全局自增时间戳，用来模拟推文发布的绝对时间先后。
        2. self.tweet_map: 存储每个用户发布的推文列表
           格式：userId -> [(-time, tweetId), (-time, tweetId), ...]
           注：Python 默认是小顶堆，存 -time 可以直接利用小顶堆弹出时间最新（绝对值最小的负数）的推文。
        3. self.follow_map: 存储每个用户关注的人的集合
           格式：followerId -> set(followeeId1, followeeId2, ...)
        """
        self.time = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        用户 userId 发布了一条新推文 tweetId。
        时间复杂度：O(1)
        """
        self.time += 1
        # 将 (-时间戳, tweetId) 追加到该用户的推文列表中
        self.tweet_map[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        获取用户 userId 的 News Feed（最多 10 条最新的推文）。
        包含：用户自己 + 用户关注的所有人。
        
        核心考点：多路归并（K-Way Merge）利用堆高效合并有序列表。
        时间复杂度：O(K + 10 log K)，其中 K 是用户关注的人数。
        空间复杂度：O(K) 堆的大小不超过关注人数。
        """
        min_heap = []
        res = []
        
        # 步骤 1：获取该用户需要展示推文的所有目标用户集合（关注者 + 自己）
        users_to_fetch = set(self.follow_map[userId])
        users_to_fetch.add(userId)  # 务必把用户自己加进去
        
        # 步骤 2：多路归并初始化
        # 将每个相关用户的【最新一条推文】放入堆中
        # 堆元素格式：(负时间戳, tweetId, userId, 该推文在用户列表中的索引 index)
        for u_id in users_to_fetch:
            if self.tweet_map[u_id]:
                last_idx = len(self.tweet_map[u_id]) - 1
                neg_time, tweet_id = self.tweet_map[u_id][last_idx]
                # 入堆
                heapq.heappush(min_heap, (neg_time, tweet_id, u_id, last_idx))
        
        # 步骤 3：最多弹出 10 次，依次获取全局最新推文
        while min_heap and len(res) < 10:
            neg_time, tweet_id, u_id, idx = heapq.heappop(min_heap)
            res.append(tweet_id)
            
            # 如果该用户还有更早的推文（idx - 1 >= 0），将前一条推文推入堆中
            if idx > 0:
                prev_idx = idx - 1
                prev_neg_time, prev_tweet_id = self.tweet_map[u_id][prev_idx]
                heapq.heappush(min_heap, (prev_neg_time, prev_tweet_id, u_id, prev_idx))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        followerId 关注 followeeId。
        注意：不能关注自己（虽然加了防御判断，但即使关注了也不影响逻辑）。
        时间复杂度：O(1)
        """
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        followerId 取消关注 followeeId。
        注意：使用 discard 避免当未关注时抛出 KeyError。
        时间复杂度：O(1)
        """
        if followerId != followeeId:
            # set.discard() 安全删除元素，若不存在不会报错
            self.follow_map[followerId].discard(followeeId)

# ================= 复习速记卡 =================
# 1. 考点组合：Hash Table + Set + K-Way Merge (堆多路归并)
# 2. 关键细节：
#    - News Feed 必须包含【自己】的推文，所以在查询前 users_to_fetch.add(userId)。
#    - unfollow 时使用 set.discard() 替代 set.remove()，避免用户取关未关注的人时报错。
#    - 堆中保存推文所在列表的 index，方便弹出后把前一条 (idx - 1) 继续放进堆中。
# =============================================