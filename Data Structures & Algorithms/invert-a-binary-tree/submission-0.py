# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        核心考点：
        - 树的递归与分治思想 (Divide and Conquer / DFS)。
        - 树节点的指针原地交换。
        
        时间复杂度：O(N) - 必须遍历树中的所有 N 个节点
        空间复杂度：O(H) - 递归调用栈深度，H 为树的高度（最好 O(log N)，最坏退化为链表 O(N)）
        """
        # 步骤 1：递归基准条件（Base Case）
        # 如果当前节点为空（遍历到底部叶子节点的后继），无需翻转，直接返回 None
        if not root:
            return None
            
        # 步骤 2：原地交换当前节点的左、右子树指针
        # Python 优雅的多变量同时赋值，无需显式写 temp 中间变量
        root.left, root.right = root.right, root.left
        
        # 步骤 3：递归去翻转已经交换过位置的左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 步骤 4：返回翻转完成后的根节点
        return root

# ================= 复习速记卡 =================
# 1. 递归口诀：
#    - 判空停递归 (if not root: return None)
#    - 交换左右子 (root.left, root.right = root.right, root.left)
#    - 递归子树走 (self.invertTree(root.left); self.invertTree(root.right))
# 2. 树指针操作千万不能用 len() 和下标遍历。
# =============================================