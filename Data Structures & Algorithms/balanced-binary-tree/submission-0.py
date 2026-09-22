# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        核心考点：
        - 自底向上的后序遍历 (Bottom-Up DFS)。
        - 剪枝/熔断设计：返回高度的同时，用 -1 标记失衡状态。
        
        时间复杂度：O(N) - 每个节点只被遍历一次
        空间复杂度：O(H) - 递归调用栈空间，H 为树的高度
        """
        def check_height(node: Optional[TreeNode]) -> int:
            """
            辅助函数：
            - 若子树平衡：返回该子树的真实最大高度 (>= 0)
            - 若子树不平衡：直接返回 -1 进行熔断
            """
            # Base Case：空节点平衡，高度为 0
            if not node:
                return 0
                
            # 步骤 1：递归检查左子树
            left_height = check_height(node.left)
            # 剪枝：如果左子树已经失衡，无需继续计算，直接向上传递 -1
            if left_height == -1:
                return -1
                
            # 步骤 2：递归检查右子树
            right_height = check_height(node.right)
            # 剪枝：如果右子树已经失衡，直接向上传递 -1
            if right_height == -1:
                return -1
                
            # 步骤 3：检查当前节点的左右高度差是否超过 1
            if abs(left_height - right_height) > 1:
                return -1
                
            # 步骤 4：当前节点平衡，向上返回当前子树的真实高度
            return 1 + max(left_height, right_height)
            
        # 只要根节点的返回值不是 -1，就说明整棵树都是高度平衡的
        return check_height(root) != -1

# ================= 复习速记卡 =================
# 1. 核心思想：后序遍历算高度 + -1 熔断标记。
# 2. 剪枝三连判：
#    - left == -1 -> return -1
#    - right == -1 -> return -1
#    - abs(left - right) > 1 -> return -1
# 3. 为什么是 O(N)：自底向上只算一次高度，遇到失衡立刻一路 return -1 退出。
# =============================================