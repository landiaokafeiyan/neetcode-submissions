
# 因为 arr 已经升序，所以答案一定是一个连续子数组。最直观的方法其实是 Two Pointers 缩窗口：sorted array
# +
# answer is contiguous
# +
# shrink from both end sorted 数组里，k 个最近的元素一定是连续的一段 → 双指针从两端开始，每次砍掉离 x 更远的那一端，剩 k 个为止。In a sorted array the k closest form a contiguous block. Shrink from the farther end until k remain; ties keep the smaller. O(n)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1

        while r - l + 1 > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1

        return arr[l:r + 1]



