class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
# 时间复杂度：O(n log n)，主要来自排序。
# 空间复杂度：O(n)，因为 sorted() 会创建新的列表。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True