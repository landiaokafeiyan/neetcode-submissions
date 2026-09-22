# for left in range(n):
#     for right in range(left + 1, n):
#         area = min(height[left], height[right]) * (right - left)
# The brute-force solution checks every possible pair of lines, so it takes O(n²) time. With two pointers, each pointer only moves inward and never moves back, so the total number of pointer movements is at most O(n). Therefore, the two-pointer solution runs in O(n) time and O(1) extra space. This is asymptotically optimal because we need to inspect the input heights at least once.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
#         I would use two pointers, one starting at the left end of the array and the other starting at the right end.

# For any pair of lines, the container area is the distance between the pointers multiplied by the shorter of the two heights. I calculate this area, update the maximum area seen so far, and then decide which pointer to move.

# If the left height is smaller, I move the left pointer to the right. If the right height is smaller or equal, I move the right pointer to the left.

# The reason is that the shorter line limits the current container height. Moving the taller line only decreases the width, while the shorter line still limits the height, so it cannot produce a better result. To possibly increase the area, I need to replace the shorter line with a taller one.

# I continue while `left < right`. This condition is sufficient because the pointers start at valid array boundaries and only move inward. When they meet, the width becomes zero, so there is no valid container left to evaluate.

# The time complexity is O(n), because each pointer moves across the array at most once. The extra space complexity is O(1).
