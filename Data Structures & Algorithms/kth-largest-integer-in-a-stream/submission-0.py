import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # 将 nums 中的元素逐个压入堆，并保持堆大小不超过 k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # 1. 将新元素压入最小堆
        heapq.heappush(self.min_heap, val)
        
        # 2. 如果堆的大小超过了 k，弹出堆顶（即当前最小的元素）
        # 这样堆里永远只留下最大的 k 个元素
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # 3. 此时堆顶（heap[0]）就是整个数据流中的第 k 大元素
        return self.min_heap[0]