# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        核心考点：
        - 双树同步 DFS 递归遍历。
        - 递归基准条件（Base Cases）的完备性覆盖。
        
        时间复杂度：O(min(N, M)) - N 和 M 分别为两棵树的节点数。只要遇到结构或数值不同就会提前短路返回。
        空间复杂度：O(min(H1, H2)) - 递归调用栈空间，取决于较矮那棵树的高度。
        """
        # 边界条件 1：两个节点均为空，说明走到了底且完全一致
        if not p and not q:
            return True
            
        # 边界条件 2：其中一个为空，另一个不为空（结构不匹配）
        if not p or not q:
            return False
            
        # 边界条件 3：两个节点都在，但节点值不同（数值不匹配）
        if p.val != q.val:
            return False
            
        # 步骤 4：当前节点完全匹配，递归比对左子树与右子树
        # 必须同时满足：p 的左子树 == q 的左子树 且 p 的右子树 == q 的右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ================= 复习速记卡 =================
# 1. 递归三步判定法（Base Cases 顺序极度关键）：
#    - 判双空：not p and not q -> True
#    - 判单空：not p or not q  -> False  (经过第一步后，这一步必定代表一空一非空)
#    - 判值异：p.val != q.val  -> False
# 2. 递归递推：
#    - return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
# =============================================