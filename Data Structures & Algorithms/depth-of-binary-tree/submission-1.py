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

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        核心考点：
        - 树的后序遍历 / 分治递归思维 (Divide and Conquer)。
        - 树深度的数学归纳：max_depth(root) = 1 + max(max_depth(left), max_depth(right))
        
        时间复杂度：O(N) - 遍历整棵树的所有节点各一次
        空间复杂度：O(H) - 递归调用栈空间，H 为树的高度（最好 O(log N)，最坏退化为链表 O(N)）
        """
        # 步骤 1：递归基准条件（Base Case）
        # 空节点的高度为 0
        if not root:
            return 0
            
        # 步骤 2：分别递归求出左子树和右子树的最大深度（分治阶段）
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 步骤 3：当前节点的最大深度 = 左右子树最大深度的较大值 + 1（当前节点自身的高度）
        return 1 + max(left_depth, right_depth)

# ================= 复习速记卡 =================
# 1. 递归极简一行流：
#    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
# 2. 递归三步曲：
#    - 明确终止条件 (not root -> 0)
#    - 明确单层逻辑 (max(left, right) + 1)
#    - 向上返回值
# =============================================
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level