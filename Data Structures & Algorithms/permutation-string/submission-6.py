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

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}
#记录s1的频次
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        l = 0
        k = len(s1)

        for r in range(len(s2)):
            ch = s2[r]
            window[ch] = window.get(ch, 0) + 1

            if r - l + 1 > k:
                left_char = s2[l]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                l += 1

            if r - l + 1 == k and window == need:
                return True

        return False

            