from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        核心考点：
        - 大顶堆（Max-Heap）实现贪心选择：永远优先做剩余次数最多的任务。
        - 队列（Queue）维护冷却期滑动窗口。
        
        时间复杂度：O(Total Cycles) - 逐步推进时间线
        空间复杂度：O(1) - 堆和队列最多容纳 26 个任务
        """
        # 步骤 1：统计各任务频次，构建大顶堆
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        cooldown_queue = deque()  # 元素格式：(剩余次数, 可以重新入堆的时间点)
        
        # 步骤 2：只要堆里还有任务，或者冷却队列里还有任务，CPU 就继续运转
        while max_heap or cooldown_queue:
            time += 1  # 推进一个 CPU 时钟周期
            
            # 如果堆中有可用任务，取出剩余次数最多的任务执行
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # 负数加 1，代表剩余次数减 1
                
                # 如果这个任务还没做完，进入冷却队列，冷却到 (time + n) 时刻解冻
                if cnt < 0:
                    cooldown_queue.append((cnt, time + n))
            
            # 检查冷却队列队头是否有任务已度过冷却期
            if cooldown_queue and cooldown_queue[0][1] == time:
                # 冷却完毕，重新推回大顶堆参与后续调度
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
                
        return time