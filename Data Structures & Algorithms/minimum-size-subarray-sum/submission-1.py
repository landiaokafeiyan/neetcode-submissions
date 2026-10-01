class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        best = float('inf')
        for r in range(len(nums)):
            total += nums[r]                 # 右端进窗口，增量维护
            while total >= target:           # 合法性谓词：和够大了
                best = min(best, r - l + 1)  # 合法时才记答案
                total -= nums[l]             # 左端滑出
                l += 1                       # 收缩
        return best if best != float('inf') else 0
# Window is valid when its sum reaches target. While valid, record the length and shrink from the left. O(n) time, O(1) space."

# 记住这个手感：最长类是"收缩到合法就停"，最短类是"合法了就往死里压"。按这个重写一遍
# state = window sum
# valid = sum >= target
# invalid = sum < target