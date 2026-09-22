class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if x==0:
            return 0
        res=1
        for i in range(abs(n)):
            res*=x
        if n>0:
            return res
        else:
            return 1/res
