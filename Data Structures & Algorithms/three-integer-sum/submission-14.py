class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i can use sorted here since it requires return the values instead of indices, then i can use twopointers
        nums=sorted(nums)
        results=[]
        for i in range(0,len(nums)-2):#先固定一个数
                    # skip duplicate fixed value
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]#compare with 0
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    results.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return results

