class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                width = r - l
                h = min(heights[l], heights[r])
                area = width * h

                max_area = max(max_area, area)

        return max_area
        #固定一个端点，移动另一个；等这个端点遍历完后，再换一个固定端点继续。只移动一个pointer 答案是不一定正确的 没有遍历到所有的情况
class Solution:#Outer loop 固定一个 pointer，inner loop 遍历另一个 pointer。这才是真正的 brute force，因为会检查所有 pair。Time: O(n²) Space: O(1)
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                width = r - l
                height = min(heights[l], heights[r])
                area = width * height

                max_area = max(max_area, area)

        return max_area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            width = r - l
            h = min(heights[l], heights[r])
            area = width * h

            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
    # A brute-force solution would check every pair of lines, which takes O(n²) time. Since the area is determined by the width and the shorter of the two heights, I can optimize this using two pointers. I start with the widest possible container. At each step, I compute the current area. Then I move the pointer corresponding to the shorter line, because the shorter line is the limiting factor. Moving the taller line would reduce the width without increasing the limiting height.