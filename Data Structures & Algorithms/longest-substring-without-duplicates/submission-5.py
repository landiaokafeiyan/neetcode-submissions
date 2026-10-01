
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_size = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_size = max(max_size, r - l + 1)
# r - l + 1和 len(s[l:r]) 不等效就是因为l:r 在list中不包含有边界 所以长度是r-l 而不是r-l+1 如果要用应该是 len(s[l:r+1])
#计算的时候直接使用r-l+1因为截取是占用额外长度的 不建议额外空间开销和时间开销 
        return max_size

