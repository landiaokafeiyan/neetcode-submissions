class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i can use sorted here since it requires return the values instead of indices, then i can use twopointers
        nums=sorted(nums)
        results=[]
        for i in range(0,len(nums)-2):#先固定一个数
                    # skip duplicate fixed value
            if i > 0 and nums[i] == nums[i - 1]:#如果当前固定的第一个数，和上一次固定的第一个数一样，那么这一轮直接跳过。
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
                    #找到一个合法 triplet 后，对 l 和 r 去重排序之后，重复值会挨在一起，所以不需要额外的 set，只要在指针移动后跳过相同的相邻值即可。
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return results

