# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        核心考点：
        - 双重 DFS 递归设计（外层遍历定位起点，内层严格比对同构）。
        - 基础母题 LeetCode 100 (Same Tree) 的模块化复用。
        
        时间复杂度：O(N * M) - 最坏情况下主树每个节点都要作为起点与 subRoot 完整比对一次 (N 为 root 节点数, M 为 subRoot 节点数)
        空间复杂度：O(max(H_root, H_sub)) - 递归调用栈的最大深度，取决于树的高度
        """
        # ================= 边界条件处理 (Base Cases) =================
        # 1. 如果 subRoot 为空树，空树是任何树的有效子树
        if not subRoot:
            return True
            
        # 2. 如果主树 root 为空，而 subRoot 非空，必定不匹配
        if not root:
            return False
            
        # ================= 核心判定逻辑 =================
        # 3. 检查以当前 root 为起点的整棵子树，是否与 subRoot 完全相同
        if self.isSameTree(root, subRoot):
            return True
            
        # 4. 如果当前节点不匹配，递归去检查 root 的左子树或右子树中是否包含 subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        辅助函数：判断以 p 和 q 为根的两棵树是否完全相同 (LeetCode 100)
        """
        # 两节点均为空，匹配成功
        if not p and not q:
            return True
            
        # 一空一非空，或者节点值不同，匹配失败
        if not p or not q or p.val != q.val:
            return False
            
        # 递归检查对应左子树与右子树是否全部相同
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ================= 复习速记卡 =================
# 1. 递归层级拆解：
#    - 外层 isSubtree：遍历 root 的每个节点作为候选根（短路逻辑：当前相同 OR 左子树含 OR 右子树含）。
#    - 内层 isSameTree：严格判定两棵子树全等（短路逻辑：值相同 AND 左子树同 AND 右子树同）。
# 2. 边界陷阱：
#    - subRoot 为 None 时直接返回 True。
#    - 只有在 root 为 None 且 subRoot 不为 None 时才返回 False。
# =============================================