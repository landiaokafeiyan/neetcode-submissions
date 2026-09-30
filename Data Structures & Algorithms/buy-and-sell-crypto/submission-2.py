class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit

# A brute-force approach would try every buy-and-sell pair, which takes O(n²). We can optimize this by scanning once from left to right. I maintain the minimum price seen so far as the best buying price. For each current price, I calculate the profit if I sell today, then update the maximum profit.”
# 一个主要移动指针 + 一个记录最佳买入位置的指针
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

# DP = 把一个大问题拆成重复子问题，并把子问题答案保存下来，避免重复计算。

# 你先记三个核心问题：
# 1. State 是什么？也就是 dp[i] 到底代表什么。
# 2. Transition 是什么？也就是当前状态怎么从前面的状态推出来。
# 3. Base case 是什么？也就是最小问题的答案是什么。       
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP