class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_freq = 0
        res = 0

        for r in range(len(s)):
            char = s[r]

            count[char] = count.get(char, 0) + 1
            max_freq = max(max_freq, count[char])

            while (r - l + 1) - max_freq > k:#Window is valid if its length minus the most frequent char count is at most k. Shrink from the left otherwise. O(n)
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res