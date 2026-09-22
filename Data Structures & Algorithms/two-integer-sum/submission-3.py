class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}#key is the value, value is the index. val->index
        for i,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return[seen[diff],i]
                # return[i,seen[diff]]
            seen[num]=i
        return []
    # [seen[diff], i]：返回的是 [较小的索引, 较大的索引]。因为 seen[diff] 是先遍历到的元素，i 是后遍历到的元素，所以索引是按升序排列的（符合大多数人的阅读习惯）。

# [i, seen[diff]]：返回的是 [较大的索引, 较小的索引]。
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}  # key 是数值，value 是对应的下标
        
#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in seen:
#                 return [seen[diff], i]  # 找到了匹配的两个下标
#             seen[num] = i  # 没找到就把当前数值和下标存入字典
            
#         return []  # 遍历完都没找到，返回空列表（题目保证有解，通常不会执行到这）

