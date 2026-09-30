class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            total=numbers[l]+numbers[r]
            if total<target:
                l+=1
            elif total>target:
                r-=1
            else:
                return [l+1,r+1]
        return []
# he key constraint is that the input array is sorted. That allows me to use two pointers. I initialize one pointer at the beginning and one at the end. If the current sum is smaller than the target, I move the left pointer right because I need a larger value. If the sum is larger than the target, I move the right pointer left. If the sum matches the target, I return the two 1-indexed positions.