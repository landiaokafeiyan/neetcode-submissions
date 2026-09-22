class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
# 定义递归函数 dfs(i)：表示从索引 i 开始到字符串末尾 s[i:] 的有效解码总数。
# 2. 代码逻辑拆解
# 边界与基础状态：
# dp = {len(s) : 1} 表示当处理到字符串末尾（空后缀）时，代表找到了一种有效的完整解码路径，方案数记为 1。

# 记忆化剪枝：
# if i in dp: return dp[i]，如果索引 i 的结果已经计算过，直接返回缓存值。

# 前导零处理：
# if s[i] == "0": return 0，单独的 '0' 无法映射到任何字母，且不能作为两位数的前导数字，因此以 '0' 开头的子串组合数为 0。

# 状态转移：

# 单字符解码：优先尝试将 s[i] 解码为一个字母（1-9），方案数为 res = dfs(i + 1)。

# 双字符解码：检查 s[i:i+2] 是否构成范围在 10 到 26 之间的有效数字：

# 若 s[i] == "1"（对应 10-19）；

# 或 s[i] == "2" 且下一个字符在 "0123456" 中（对应 20-26）。

# 满足条件时，可将两字符组合解码为一个字母，累加方案数：res += dfs(i + 2)。

# 结果缓存与返回：
# 将计算得到的 res 存入 dp[i] 并返回。最终调用 dfs(0) 即可获取全串的解码方案数。
# 利用哈希表 dp 记录已计算过的 dfs(i) 结果，避免重复递归计算。
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = (i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res +=dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]