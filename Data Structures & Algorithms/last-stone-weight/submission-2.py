import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        核心考点：
        - 大顶堆（Max-Heap）模拟贪心/碰撞过程。
        - Python 默认是最小堆，通过【存相反数（负数）】来实现大顶堆。
        
        时间复杂度：O(N log N) - 每次碰撞弹出两个元素、最多推入一个元素，循环最多 N 次，每次堆操作 O(log N)
        空间复杂度：O(N) - 存储堆所用的列表空间
        """
        
        # 步骤 1：将所有石头的重量取负数，构建大顶堆的数据源
        # 例如：[2, 7, 4, 1, 8, 1] -> [-2, -7, -4, -1, -8, -1]
        max_heap = [-w for w in stones]
        
        # 步骤 2：原地堆化，耗时 O(N)
        # 堆化后，最小的负数（即原本最重的石头）排在堆顶 max_heap[0]
        heapq.heapify(max_heap)
        
        # 步骤 3：只要还有至少 2 块石头，就持续取出最重的两块进行粉碎
        while len(max_heap) >= 2:
            # 弹出并还原第一重、第二重的石头重量
            # 注意：heappop 会直接从堆中移除堆顶元素
            first = -heapq.heappop(max_heap)   # 最重的石头
            second = -heapq.heappop(max_heap)  # 第二重的石头
            
            # 如果两块石头重量不相等，剩下 (first - second) 重量的新石头重新放回堆中
            # 因为 first 肯定是最大的，所以 first >= second 永远成立
            if first > second:
                remained = first - second
                # 重新以负数形式推入大顶堆
                heapq.heappush(max_heap, -remained)
                
            # 如果 first == second，两块石头完全粉碎，无需推入任何新元素
            
        # 步骤 4：处理最终结果
        # 如果堆中还剩 1 块石头，弹出并还原为正数返回；如果全碎了（堆为空），返回 0
        return -max_heap[0] if max_heap else 0

# ================= 复习速记卡 =================
# 1. 大顶堆模板写法：
#    - 进堆：heapq.heappush(heap, -val)
#    - 出堆：val = -heapq.heappop(heap)
#    - 堆化：heap = [-x for x in nums]; heapq.heapify(heap)
# 2. 终止条件：len(heap) >= 2（至少需要两块石头才能碰）
# 3. 边界防御：最后堆可能为空，返回前判断 if max_heap else 0
# =============================================