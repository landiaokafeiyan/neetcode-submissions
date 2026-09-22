# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        核心考点：
        - 广度优先搜索 (BFS) 与双端队列 (deque) 的标准结合。
        - 利用 len(queue) 快照机制实现分层处理与隔离。
        
        时间复杂度：O(N) - 树中每个节点恰好入队一次、出队一次。
        空间复杂度：O(W) - 队列中最多同时存放最大一层的节点数（W <= N/2）。
        """
        # 边界处理：空树直接返回空列表
        if not root:
            return []
            
        res = []
        # 初始化双端队列，将根节点推入作为第 0 层
        queue = deque([root])
        
        # 外层循环：逐层向下遍历，直到队列为空
        while queue:
            # 步骤 1：获取当前层的节点总数（核心技巧：固定当前层的长度快照）
            level_size = len(queue)
            current_level_vals = []
            
            # 步骤 2：精确弹出并处理当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                current_level_vals.append(node.val)
                
                # 步骤 3：将下一层的左右子节点按从左到右顺序加入队尾
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # 步骤 4：将当前层的结果列表追加到全局结果中
            res.append(current_level_vals)
            
        return res

# ================= 复习速记卡 =================
# 1. 核心骨架：
#    queue = deque([root])
#    while queue:
#        level_size = len(queue)
#        for _ in range(level_size):
#            node = queue.popleft()
#            ...
# 2. 必须用 len(queue) 提前锁定当前层大小，不能在 for 循环中动态计算队列长度。
# =============================================