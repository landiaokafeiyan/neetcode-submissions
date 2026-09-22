import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        核心考点：
        - 维护固定容量为 k 的最小堆（Min-Heap）。
        - 堆顶就是这 k 个最大数里的最小值（即第 k 大）。
        
        时间复杂度：O(N log k) - 堆的最大容量被限制在 k，插入/弹出耗时 O(log k)
        空间复杂度：O(k) - 仅需存储 k 个元素
        """
        min_heap = []
        
        for num in nums:
            # 步骤 1：堆未装满 k 个时，直接入堆
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            # 步骤 2：堆满后，如果新数字比堆顶大，替换掉堆顶
            elif num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        # 步骤 3：堆顶即为第 k 大元素
        return min_heap[0]
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        思路：
        - 取相反数构建大顶堆。
        - 连续弹出 k 次，第 k 次弹出的即为第 k 大元素。
        
        时间复杂度：O(N + k log N) - 线性建堆 O(N)，弹出 k 次 O(k log N)
        空间复杂度：O(N) - 需要存储全量负数列表
        """
        # 步骤 1：转为负数构建大顶堆
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        
        # 步骤 2：弹出前 k - 1 个最大的数
        for _ in range(k - 1):
            heapq.heappop(max_heap)
            
        # 步骤 3：第 k 次弹出的就是目标答案（取负数还原）
        return -heapq.heappop(max_heap)
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlargest(k, nums) 返回前 k 个最大元素的降序列表，[-1] 就是第 k 个
        return heapq.nlargest(k, nums)[-1]