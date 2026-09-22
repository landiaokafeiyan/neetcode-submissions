import sys

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # 提高 Python 的递归深度限制以防止爆栈
        sys.setrecursionlimit(20000)
        
        memo = {}
        
        def dfs(amt: int) -> float:
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            
            res = float('inf')
            for coin in coins:
                if amt - coin >= 0:
                    # 使用 Python 内置的 min 函数
                    res = min(res, 1 + dfs(amt - coin))
                    
            memo[amt] = res
            return res
            
        min_coins = dfs(amount)
        return int(min_coins) if min_coins != float('inf') else -1
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] 表示凑成金额 i 所需的最少硬币数
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != float('inf') else -1