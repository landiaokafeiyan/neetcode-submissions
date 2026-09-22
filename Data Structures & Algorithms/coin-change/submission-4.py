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