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
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1#为什么只跳过 l 就够了，不需要跳过 r 跳过一个就避免重复了

        return res