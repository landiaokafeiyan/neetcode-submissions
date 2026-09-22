class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])

        return dp[n]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))
# DP is based on combining solutions to subproblems to yield a solution to the original problem.L6 级别的 DP，本质上是 "带备忘录的 DFS" (DFS + Memoization)

# 核心概念：DP = 递归 + 缓存
# 不要把 DP 想成数学归纳法。对于面试，请把 DP 看作：

# "我们遍历了所有可能的情况（暴力搜索），但是聪明的记录下了每一步的结果，保证同样的坑不踩两次。"

# 要素一：状态定义 (State Definition)
# —— “数组的每个格子 dp[i] 代表什么人话？”

# 这是最难的一步。如果定义错了，后面全错。

# 常见套路：

# 结尾型： dp[i] = 以第 i 个元素结尾的...（如：最大子数组和、LIS）。

# 范围型： dp[i][j] = 从下标 i 到 j 的区间内的...（如：回文子串）。

# 资源型（背包）： dp[i][w] = 前 i 个物品，占用 w 容量时的...。

# L6 考核点： 能否处理 多维状态？

# 例如： 买卖股票系列。光有 dp[i] (天数) 不够，还得加维度：dp[i][k][0/1] (第 i 天，交易了 k 次，手头持有/不持有股票)。

# 要素二：状态转移方程 (Transition Function)
# —— “我怎么从之前的状态算出现在的状态？”

# 本质就是 “做选择” (Make a Choice)。

# 核心逻辑：

# 选还是不选？ (Knapsack: max(dp[i-1][w], dp[i-1][w-weight] + value))

# 从哪跳过来？ (Climbing Stairs: dp[i] = dp[i-1] + dp[i-2])

# 跟谁拼起来？ (Word Break: dp[i] = dp[j] && check(s[j:i]))

# L6 考核点： 能否用 数学归纳法 清晰地解释为什么这个方程覆盖了所有情况（MECE原则 - 完全穷尽，互不重复）。

# 要素三：初始化与边界 (Base Case)
# —— “多米诺骨牌的第一块怎么推？”

# 常见坑点：

# dp 数组通常要开 N+1 的大小，让 dp[0] 代表“空”或“初始”。

# 求最大值时，初始化为 0 或 -inf；求最小值时，初始化为 inf。

# L6 考核点： 处理 Edge Case（如数组为空、容量为0）时的代码鲁棒性。

# 要素四：计算顺序 (Iteration Order)
# —— “填表的顺序是啥？”

# 绝大多数： 从左到右，从上到下。

# 区间 DP： 按照“区间长度”从小到大遍历（先算长度为 2 的，再算长度为 3 的）。

# 背包优化： 1D 数组时，内层循环是从右向左（Reverse），防止重复利用同一层的数据。

# L6 必杀策略：Top-Down vs Bottom-Up
# 这是区分 L4 和 L6 的关键分水岭。

# 策略建议：面试时，优先写 Top-Down (记忆化搜索)，除非被要求优化空间。

# 1. Top-Down (DFS + Memoization)
# 写法： 写一个递归函数 dfs(state)，开头加一句 if state in memo: return memo[state]。

# 优点：

# 符合人类直觉： 自顶向下思考（我要解决大问题，必须先解决子问题）。

# 处理稀疏状态： 如果 DP 表很大但实际访问的状态很少，Top-Down 极其节省空间和时间。

# 易于实现： 不需要考虑复杂的遍历顺序（斜着遍历？倒着遍历？）。

# L6 话术： "I'll start with a Top-Down approach with Memoization. It's more intuitive to map the recursion tree directly, and it avoids computing unreachable states."

# 2. Bottom-Up (Tabulation)
# 写法： for i in range... for j in range...

# 优点：

# 空间优化 (Rolling Array): 这是唯一的绝对优势。只有 Bottom-Up 才能把 O(N^2) 空间优化成 O(N) 甚至 O(1)。

# L6 话术： "Now that we have the recurrence relation working, I can optimize the space complexity from O(N) to O(1) using the Bottom-Up iterative approach, since dp[i] only depends on dp[i-1]."

# 总结：如何高效复习？
# 不要刷太多题，把下面这 3 类母题 吃透，记住它们的状态定义：

# 坐标/路径类 (Grid):

# 代表作： Unique Paths, Minimum Path Sum.

# 核心： dp[i][j] 只跟左边和上边有关。

# 序列/双串类 (Sequence):

# 代表作： Longest Common Subsequence (LCS), Edit Distance.

# 核心： dp[i][j] 代表 s1 前 i 个字符和 s2 前 j 个字符的关系。

# 背包/组合类 (Knapsack):

# 代表作： Coin Change, Partition Equal Subset Sum.

# 核心： 外层循环遍历物品，内层循环遍历容量。

# 一句话心法： DP 就是带着记事本的 DFS。先写 DFS，发现有重复计算，加上 @cache (Python) 或 memo 字典，你就做出了 DP。




# 针对 Google L6 (Staff) 的 Coding 面试，你的解题思路不能只停留在“把题做出来”。你需要展示的是**“Tech Lead 解决工程问题的标准流程”**。

# 面试官在考察你时，脑子里想的是：“如果我把这个复杂的任务交给这个人，他会直接瞎写，还是会先分析清楚再动手？他写的代码以后好维护吗？”

# 以下是为你定制的 L6 标准解题五步法 (The 5-Step Framework)。请刻意练习这个节奏。

# 第一步：Clarify & Define (澄清与定义) —— 占时 3-5 分钟
# 目标： 消除模糊性 (Ambiguity)，界定边界 (Scope)。L6 最忌讳上来就写。

# 动作 1：复述问题。 确保你理解的跟面试官想的一样。

# 动作 2：挖掘约束 (Constraints)。

# 输入规模： "N 是多少？100 还是 10亿？"（决定了是 O(N^2) 还是 O(N) 甚至 O(logN)）。

# 数据类型： "有负数吗？有空值吗？是稀疏矩阵吗？"

# 内存限制： "能把所有数据加载进内存吗？还是需要处理 Stream？"

# L6 加分话术：

# "Is this a one-time script or a production service? If it's production, I should handle exceptions more gracefully." (这是脚本还是生产服务？这决定了代码的健壮性要求。)

# 第二步：Example & Strategy (举例与策略) —— 占时 5-8 分钟
# 目标： 展示思维过程，确定算法方案。

# 动作 1：画图与举例。 在白板/文档上列出几个 Case。

# Normal Case: 普通输入。

# Edge Case: 空列表、只有一个元素、全重复元素。

# 动作 2：方案对比 (Trade-off)。 这是 L6 的核心。

# 不要直接说最优解。先说：“最直观的方法是暴力法 O(N^2)，但在 N 很大时不可行。”

# 再说：“我们可以优化。我想到两种方案：方案 A 用 HashMap 换时间 (Time O(N), Space O(N))；方案 B 用排序 (Time O(NlogN), Space O(1))。”

# 决策： "Given we prioritize latency over memory here, I will choose Approach 