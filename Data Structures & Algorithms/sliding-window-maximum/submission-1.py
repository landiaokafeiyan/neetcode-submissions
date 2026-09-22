from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        核心考点：
        # 在 Python 的 deque 中，q[0] 是最左边（队头），q[-1] 是最右边（队尾）。
        - 单调队列（Monotonic Queue）优化定长滑动窗口极值问题。
        - 队列中只存储【数组下标】，且对应的值保持【从大到小严格单调递减】。
        
        时间复杂度：O(N) - 每个元素的下标最多被 append 进队一次，被 pop 出队一次。
        空间复杂度：O(k) - 双端队列中最多同时存放 k 个元素的下标。
        """
        # q 存储的是元素在 nums 中的下标 index
        q = deque()
        res = []
        
        for r in range(len(nums)):
            # 步骤 1：淘汰队尾比当前元素小的所有下标（破坏单调性的元素全部滚蛋）
            # 核心思想：既然 nums[r] 比你大，还比你年轻（晚离开窗口），你就永远没机会当最大值了
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            # 将当前右边界下标加入队尾
            q.append(r)
            
            # 步骤 2：检查队头元素是否已滑出当前窗口左边界
            # 当前合法窗口范围为 [r - k + 1, r]，如果队头下标小于左边界，直接从队头剔除
            if q[0] < r - k + 1:
                q.popleft()
                
            # 步骤 3：当窗口大小达到 k 时，开始收集答案
            # 队头 q[0] 必定是当前窗口内的最大值所在下标
            if r >= k - 1:
                res.append(nums[q[0]])
                
        return res

# ================= 复习速记卡 =================
# 1. 核心数据结构：collections.deque()（双端队列，两头均可 O(1) 弹出）。
# 2. 存下标而非存值：存下标既能比大小 (nums[q[i]])，又能判过期 (q[0] < r - k + 1)。
# 3. 两个弹出条件：
#    - 队尾 pop：nums[q[-1]] < nums[r]（维护从大到小单调性）。
#    - 队头 popleft：q[0] < r - k + 1（淘汰过期滑出窗口的元素）。
# =============================================