class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
# In Python, HashSet is implemented as a set, and HashMap is implemented as a dict (dictionary).

# The primary difference is what they store: a set stores unique individual elements, whereas a dictionary stores key-value pairs.
# Core DifferencesFeaturePython set (HashSet)Python dict (HashMap)Data StructureStores unique values onlyStores key-value pairsSyntax{1, 2, 3}{"a": 1, "b": 2}Lookup TargetChecks if an item existsLooks up a value by keyDuplicatesNo duplicate elements allowedDuplicate values allowed; keys must be uniqueKey RequirementElements must be hashable (immutable)Keys must be hashable; values can be anythingTime Complexity$O(1)$ average for in, add(), remove()$O(1)$ average for get(), [], in (keys)