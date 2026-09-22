class Solution:
    def reverseBits(self, n: int) -> int:
    # def reverseBits(n):
        result = 0

        for _ in range(32):
            bit = n & 1 #取出来当前bit
            result = (result << 1) | bit#result = result * 2 + bit左移一位 = 给二进制末尾添加一个 0；再 OR 一个 bit = 把这个 0 改成我们需要的 bit。
            n >>= 1#进行下一位

        return result