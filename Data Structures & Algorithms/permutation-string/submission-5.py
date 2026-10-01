from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        l = 0
        k = len(s1)

        for r in range(len(s2)):
            window[s2[r]] += 1

            if r - l + 1 > k:
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            if r - l + 1 == k and window == need:
                return True

        return False


def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    c1, window = Counter(s1), Counter()
    for r in range(len(s2)):
        window[s2[r]] += 1
        if r >= len(s1):                       # 窗口超了，滑出左端
            window[s2[r - len(s1)]] -= 1
        if window == c1:                       # 合法性谓词：频次相等
            return True
    return False

            