# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         res=[0]*n

#         for i in range(n):
#             prod=1
#             for j in range(n):
#                 if i==j:
#                     continue
#                 prod*=nums[j]
#             res[i]=prod
#         return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res      