
        # count the frequencies → sort by frequency → take the top k.
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 手动用 dict 统计频次
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. 将字典按 value（频次）降序排序
        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # 3. 取前 k 个
        return sorted_elements[:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计每个数字出现的频次 (Count the frequencies)
        # 例如: nums = [1,1,1,2,2,3] -> count = {1: 3, 2: 2, 3: 1}
        count = Counter(nums)
        
        # 2. 按照频次从大到小对所有的 key 进行降序排序 (Sort by frequency)
        # key=lambda x: count[x] 表示比较的是字典中记录的出现频次
        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # 3. 截取前 k 个元素返回 (Take the top k)
        return sorted_elements[:k]

# 因为当面对海量数据流（Stream Data，无法一次性加载到内存或桶中）时，维护一个固定容量为 $k$ 的小顶堆可以在空间受限的情况下高效找出 Top K。



import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 统计每个数字出现的频次 -> O(N)
        count = Counter(nums)
        
        # 2. 维护一个大小为 k 的最小堆 Python 中 heapq 默认就是最小堆（Min-Heap），堆顶（heap[0]） 永远是全堆的全局最小值。
        # 只有当你依次从堆中 heappop() 弹出元素时，弹出的序列才是严格升序（从小到大）的！
        min_heap = []
        
        for num, freq in count.items():
            # 关键：以元组 (freq, num) 入堆，heapq 默认以元组的第一个元素（freq）作为比较依据
            heapq.heappush(min_heap, (freq, num))
            
            # 如果堆的大小超过了 k，把堆顶（当前频次最小的元素）弹出 -> O(log k)
            if len(min_heap) > k:
                heapq.heappop(min_heap)#每次都把最小给pop出去了 剔除
                
        # 3. 此时堆中剩下的 k 个元素就是出现频次最高的 k 个数字
        # 从 (freq, num) 中提取出数字 num
        return [num for freq, num in min_heap]