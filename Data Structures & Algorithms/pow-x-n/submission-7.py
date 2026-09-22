# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if x == 0:
#             return 0
#         if n == 0:
#             return 1

#         res = 1
#         for i in range(abs(n)):
#             res *= x
#         return res if n >= 0 else 1 / res
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power:
            if power & 1:# odd or even取代耗时相对高一点的取模运算 power % 2 != 0
                res *= x
            x *= x
            power >>= 1#每经过一次循环，指数 power 减半

        return res if n >= 0 else 1 / res