# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心考点：
        - 广度优先搜索 (BFS) 层序遍历。
        - 快照分层：每层只提取最后一个被访问的节点。
        
        时间复杂度：O(N) - 遍历树中所有 N 个节点
        空间复杂度：O(W) - W 为二叉树的最大宽度（最底层最多 N/2 个节点）
        """
        # 边界处理：空树直接返回空列表
        if not root:
            return []
            
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # 关键判定：如果是当前层的最后一个节点，记录到右视图结果中
                if i == level_size - 1:
                    res.append(node.val)
                    
                # 按照从左到右的顺序将子节点入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res

# ================= 复习速记卡 =================
# 1. 骨架：标准 BFS 层序遍历。
# 2. 关键点：if i == level_size - 1: res.append(node.val)
# 3. 为什么正确：每层从左往右入队，最后一个出队的一定是视野最右边的节点。
# =============================================

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        核心考点：
        - 深度优先搜索 (DFS) 先右后左遍历。
        - 深度与结果列表长度比对：depth == len(res) 首次捕获每层最右节点。
        
        时间复杂度：O(N) - 遍历所有节点
        空间复杂度：O(H) - 递归栈深度，H 为树的高度（最好 O(log N)，最坏 O(N)）
        """
        res = []
        
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
                
            # 如果当前深度还没有记录过节点，说明当前节点是该层首次访问的节点（即最右节点）
            if depth == len(res):
                res.append(node.val)
                
            # 关键：先递归右子树，再递归左子树！
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return res

# ================= 复习速记卡 =================
# 1. 遍历顺序反转：根 -> 右 -> 左。
# 2. 去重技巧：depth == len(res) 确保每层只有最先被访问的“右侧第一人”能入选。
# =============================================