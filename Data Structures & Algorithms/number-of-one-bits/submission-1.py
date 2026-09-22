class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            # 判断最低位是否是 1
            if n & 1:
                count += 1
            # 整体右移一位，处理下一位
            n >>= 1
        return count