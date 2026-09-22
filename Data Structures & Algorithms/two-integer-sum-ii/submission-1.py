class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
    
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}  # key: 数值, value: 对应的 1-indexed 索引
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in seen:
                return [seen[diff], i + 1]
            seen[n] = i + 1
            
        return []
