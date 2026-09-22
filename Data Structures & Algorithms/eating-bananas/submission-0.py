
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            k = l + (r - l) // 2

            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                r = k
            else:
                l = k + 1

        return l