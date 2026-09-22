import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        初始化对象：维护一个容量最多为 k 的小顶堆（Min-Heap）。
        
        核心思维模型：
        - 找第 K 大元素 -> 维护容量为 K 的最小堆。
        - 堆里只留下全局最大的 K 个数。
        - 堆顶 (min_heap[0]) 是这 K 个大数里的最小值，也就是我们要找的【第 K 大】。
        """
        self.k = k
        self.min_heap = nums
        
        # 步骤 1：原地将列表转换为小顶堆结构
        # 时间复杂度：O(N) 线性建堆，比逐个 heappush 更快
        heapq.heapify(self.min_heap)
        
        # 步骤 2：淘汰掉多余的较小元素，只保留前 k 个最大的数
        # 如果初始 nums 长度大于 k，不断把堆顶（当前全堆最小值）弹出
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        """
        向数据流中添加新数字，并实时返回当前的第 K 大元素。
        
        时间复杂度：O(log K) - 堆的最大容量被严格限制在 K
        空间复杂度：O(K) - 只需存储 K 个元素
        """
        # 步骤 1：如果堆还没装满 K 个元素，直接无条件压入
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        
        # 步骤 2：如果堆已经满了，且新来的数字比堆顶门槛（第 K 大）还要大
        # 说明这个新数字有资格挤进前 K 名，需要淘汰掉原堆顶，再放入新数字
        # 技巧：heappushpop 比先 push 再 pop 更高效（单次堆调整）
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
            
        # 注意：如果 val <= self.min_heap[0]，说明新数字连前 K 名都进不去，直接忽略不入堆
        
        # 步骤 3：当前堆顶就是前 K 个最大值中最小的那个，即第 K 大元素
        return self.min_heap[0]

# ================= 复习速记卡 =================
# 1. 考点：Top K 问题 / 数据流维护 / 最小堆淘汰制
# 2. 规律：求第 K 大用【小顶堆】，求第 K 小用【大顶堆】
# 3. 陷阱：初始 nums 的长度可能小于 k，因此必须先判断 len < k 再进行比较
# =============================================