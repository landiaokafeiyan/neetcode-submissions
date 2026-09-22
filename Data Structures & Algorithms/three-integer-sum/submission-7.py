class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break#因为数组已排序，如果固定数 nums[i] > 0，后面的数必定全大于 0，三个正数之和不可能等于 0，直接 break 终止循环。

            if i > 0 and a == nums[i - 1]:
                continue#外层去重：因为题目要求返回的是“数值三元组”，并且禁止出现重复的数值组合，无论下标是否相同。

# 如果 i > 0 且 nums[i] == nums[i - 1]，说明以该数值作为第一个数的所有有效组合在上一轮已经全部找齐了，直接 continue 跳过。

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:#只有找到一个合法三元组后，才需要同时移动两个指针并跳过重复值
                        l += 1#为什么只跳过 l 就够了，不需要跳过 r 跳过一个就避免重复了

        return res


#         Before I start, I would like to confirm that I need to return all unique triplets whose sum is zero, and that the output order does not matter. I would also ask whether I am allowed to modify the input array.

# The brute-force approach would enumerate every combination of three elements and check whether their sum is zero. That takes O(n³) time, so I would use it only as a baseline.

# A better approach is to fix one number and solve a Two Sum problem for the remaining numbers with a hash map. This reduces the time complexity to O(n²), but handling duplicate triplets is less clean.

# My preferred solution is to sort the array first. Sorting is safe here because the output requires the values in each triplet, not the original indices.

# Then I iterate through the array and fix one number at index i. For each fixed number, I use two pointers: left starts at i plus one, and right starts at the end of the array.

# If the sum of the three numbers is too small, I move the left pointer right to increase the sum. If the sum is too large, I move the right pointer left to decrease the sum. If the sum is zero, I add the triplet to the result and move both pointers.

# To avoid duplicate triplets, I skip duplicate values for the fixed number. After finding a valid triplet, I also skip repeated values at both the left and right pointers.

# The sorting step takes O(n log n), and the nested loop with two pointers takes O(n²), so the total time complexity is O(n²). The extra space complexity is O(1), excluding the output and the internal memory used by the sorting implementation.
