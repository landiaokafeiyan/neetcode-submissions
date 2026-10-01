from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        target = sorted(s1)

        for i in range(len(s2) - k + 1):
            substring = s2[i:i + k]

            if sorted(substring) == target:
                return True

        return False
# 窗口数量：O(n)
# 每个窗口排序：O(k log k)

# 总时间：O(n * k log k)        
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

def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    target = sorted(s1)
    for i in range(len(s2) - len(s1) + 1):
        if sorted(s2[i:i + len(s1)]) == target:
            return True
    return False   
# 这个版本的核心问题是：每移动一个窗口，都重新统计一次整个窗口。
# 而 Sliding Window 的优化就是：
# 不重新计算整个窗口，只更新“新进来的字符”和“移出去的字符”。he problem asks whether s2 contains a permutation of s1. Key observation: a permutation means exactly the same character frequencies, and it must appear as a contiguous block of length len(s1) in s2.

# A brute-force approach would check every substring of s2 of that length — that's n minus m plus 1 windows — and compare sorted or counted frequencies against s1. That costs O(n·m log m) with sorting.

# But notice adjacent windows overlap in m minus 1 characters — brute force recomputes everything from scratch. We can reuse that overlap with a fixed-size sliding window: maintain frequency counts incrementally. Each slide changes only two characters — one enters, one leaves.

# So: build a Counter for s1 once. Slide a window of size len(s1) across s2, updating counts in O(1) per step. If the window's counts ever equal s1's, return True; otherwise False after the full scan.

# Time is O(n) — each character enters and leaves once, and Counter comparison is O(26), constant. Space is O(26).       