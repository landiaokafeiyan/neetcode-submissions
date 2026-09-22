
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
# 每次 binary search，[l, r] 中至少有一半是正常排序的。先判断哪一半 sorted，再判断 target 是否落在这一半。
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 1. 如果 mid 正好是 target，直接返回
            if nums[mid] == target:
                return mid

            # 2. 判断左半边 [left, mid] 是否是正常递增的
            if nums[left] <= nums[mid]:

                # 如果 target 位于左边这个有序区间内
                if nums[left] <= target < nums[mid]:
                    # 去左半边继续找
                    right = mid - 1
                else:
                    # target 不在左边有序区间
                    # 所以去右半边
                    left = mid + 1

            # 3. 否则说明右半边 [mid, right] 一定是正常递增的
            else:

                # 如果 target 位于右边这个有序区间内
                if nums[mid] < target <= nums[right]:
                    # 去右半边继续找
                    left = mid + 1
                else:
                    # target 不在右边有序区间
                    # 所以去左半边
                    right = mid - 1

        # 整个数组都没找到
        return -1

#         I will use a modified binary search.

# At every step, I calculate the middle index. If the middle value equals the target, I return that index immediately.

# Otherwise, because the array was originally sorted and rotated only once, at least one half of the current search range must still be sorted.

# First, I check whether the left half is sorted by comparing `nums[left]` and `nums[mid]`. If `nums[left]` is less than or equal to `nums[mid]`, the left half is sorted.

# Then I check whether the target falls inside the value range of that sorted left half. Because I have already checked that `nums[mid]` is not the target, the condition is `nums[left] <= target < nums[mid]`.

# If that condition is true, I move `right` to `mid - 1` and search the left half. Otherwise, the target must be in the right half, so I move `left` to `mid + 1`.

# If the left half is not sorted, then the right half must be sorted. I check whether the target is in the range `nums[mid] < target <= nums[right]`.

# If it is, I search the right half by setting `left` to `mid + 1`. Otherwise, I search the left half by setting `right` to `mid - 1`.

# The loop continues while `left <= right`, because a single remaining element still needs to be checked.

# Each iteration discards half of the remaining search range, so the time complexity is O(log n). The algorithm uses O(1) extra space.
