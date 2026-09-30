class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #my ideas, traverse the list and save the values in a hashset, every time check if the value in the set or not, if not return Ture otherwise False
        visited=set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
