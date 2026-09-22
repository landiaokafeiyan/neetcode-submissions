
#top2bottom memories
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)

#bottom to up
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache  # 缓存递归结果，避免重复计算自顶向下的递归写法，只需要加上记忆化缓存（例如 Python 内置的 @cache），避免重复计算。时间复杂度可降至 $O(n)$。
        def dfs(n: int) -> int:
            if n <= 2:
                return n
            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1  # n = 1
        prev1 = 2  # n = 2

        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1