class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


#I would use a hash set to keep track of the numbers I have already seen.

# Then I iterate through the array once. For each number, I first check whether it is already in the set. If it is, that means this number has appeared before, so I can immediately return `True`.

# Otherwise, I add the current number to the set and continue scanning the array. If I finish the loop without finding any repeated number, I return `False`.

# This approach takes O(n) time because I scan the array once, and hash-set lookup and insertion are O(1) on average. The extra space complexity is O(n) in the worst case, when all numbers are distinct.

# For edge cases, an empty array or an array with one element returns `False`, because neither can contain duplicates.
