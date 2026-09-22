
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            k = l + (r - l) // 2

            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k#计算吃完这一堆 pile 香蕉，在每小时吃 k 个的情况下，需要多少个小时。向上取整

            if hours <= h:
                r = k
            else:
                l = k + 1

        return l