class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]

#         * **存储范围**：只有 $0 \le i \le N - 1$ 的结果会被记录到 `memo` 中，因此 `memo` 只需要保存 $N$ 个状态（索引 $0$ 到 $N - 1$），开长度为 `len(cost)` 即可。

# ---

# ### 对比总结

# | 解法 | 数组名 | 状态表达含义 | 终点 $N$ 的处理 | 所需数组长度 |
# | :--- | :--- | :--- | :--- | :--- |
# | **Bottom-Up** | `dp` | 到达第 $i$ 阶的最小开销 | 作为计算目标，保存在 `dp[n]` | **$N + 1$** |
# | **Top-Down** | `memo` | 从第 $i$ 阶出发到顶的开销 | 触发 Base Case（返回 $0$），不入缓存 | **$N$** |

# > **补充**：如果 Top-Down 的代码写成把 $i = N$ 也存进 `memo`，那 `memo` 同样需要开 $N + 1$ 的长度；但在现有的写法里，Base Case 提前把 $i \ge N$ 的情况拦截掉了，所以只开 $N$ 长度更省内存空间。