# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        核心考点：
        - 后序遍历 (左右根 / 自底向上回溯)。
        - 递归返回值的语义设计与透传机制。
        
        时间复杂度：O(N) - 最坏情况下需要遍历整棵树的所有 N 个节点
        空间复杂度：O(H) - 递归调用栈空间，H 为树的高度（最好 O(log N)，最坏退化为链表 O(N)）
        """
        # ================= 1. 递归终止条件 (Base Cases) =================
        # 情况 1: 走到了叶子节点下方的空节点，说明没找到，返回 None
        # 情况 2: 当前节点就是目标节点 p 或 q 之一，直接把当前节点向上返回
        # (注：如果 p 本身就是 q 的祖先，找到 p 后直接返回 p，上层不会再往下搜 q，逻辑依然完全正确)
        if not root or root == p or root == q:
            return root
            
        # ================= 2. 分治递归搜索子树 (Divide) =================
        # 分别去左子树和右子树寻找 p 或 q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # ================= 3. 结果合并与向上透传 (Conquer) =================
        # 情况 A: p 和 q 分布在当前节点的两侧 (左边找到了一个，右边也找到了一个)
        # 说明当前 root 正好是它们分道扬镳的最近公共祖先！
        if left and right:
            return root
            
        # 情况 B: 只有一边找到了 (left 有值或 right 有值，或者都为 None)
        # 哪边非空就返回哪边（直接向上透传找到的结果）；如果都为空则返回 None
        return left if left else right

# ================= 复习速记卡 =================
# 1. Base Case: if not root or root == p or root == q: return root
# 2. 左右递归: left = LCA(root.left), right = LCA(root.right)
# 3. 结果合并三部曲:
#    - 左右都在 (left and right) -> 当前 root 是分叉祖先，返回 root
#    - 只有一边有 (left 或 right) -> 返回非空的那一边 (left or right)
#    - 左右都没 -> 返回 None (已被 left or right 涵盖)
# =============================================