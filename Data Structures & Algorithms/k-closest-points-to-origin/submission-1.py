import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        核心考点：
        - 最小堆（Min-Heap）快速提取前 K 个最小值。
        - 距离计算简化：d^2 = x^2 + y^2（不开平方，避免浮点数开销）。
        
        时间复杂度：O(N + K log N) 
          - 线性建堆 O(N)
          - 弹出 K 次，每次 O(log N)，总计 O(K log N)
        空间复杂度：O(N) 存储所有点的元组
        """
        # 步骤 1：将每个点的 (距离平方, 坐标) 存入列表
        # 元组 (dist, [x, y])：heapq 会默认拿第 0 项 dist 作为优先级排序依据
        min_heap = [(x**2 + y**2, [x, y]) for x, y in points]
        
        # 步骤 2：原地将列表转换为小顶堆 -> O(N)
        heapq.heapify(min_heap)
        
        # 步骤 3：连续从堆顶弹出 k 次，每次弹出的都是当前全局距离最小的点
        res = []
        for _ in range(k):
            dist, point = heapq.heappop(min_heap)
            res.append(point)
            
        return res

# ================= 复习速记卡 =================
# 1. 技巧：元组 (priority_key, data) 是 heapq 自定义排序的标准写法。
# 2. 优化：不写 math.sqrt()，直接比 x^2 + y^2，速度更快且无精度误差。
# =============================================