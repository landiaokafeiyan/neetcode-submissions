# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        核心考点：
        - 后序遍历 (DFS) 递归计算子树深度。
        - 全局变量动态维护任意节点为最高转折点时的最大直径。
        
        数学模型：
        - 穿过节点 node 的最大直径 (边数) = left_depth + right_depth
        - node 向其父节点提供的最大深度 = 1 + max(left_depth, right_depth)
        
        时间复杂度：O(N) - 遍历所有节点各一次
        空间复杂度：O(H) - 递归栈深度，H 为树的高度
        """
        self.max_diameter = 0  # 全局记录历史见过的最大边数
        
        def get_depth(node: Optional[TreeNode]) -> int:
            """
            辅助函数：返回以 node 为根的子树的最大深度（节点数口径）
            """
            if not node:
                return 0
                
            # 1. 递归求出左子树和右子树的深度
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            
            # 2. 核心考点：以当前 node 为转折点的最长路径边数 = 左深度 + 右深度
            # （左深度的边数 + 右深度的边数 正好等于两边节点数之和）
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # 3. 向上层父节点贡献当前节点的最大单侧深度
            return 1 + max(left_depth, right_depth)
            
        # 触发递归
        get_depth(root)
        
        return self.max_diameter

# ================= 复习速记卡 =================
# 1. 区别：Max Depth 是自顶向下单链；Diameter 是以某节点为顶点的倒 V 形跨度。
# 2. 模式：后序遍历算深度，顺便维护全局最大直径。
# 3. 边数 vs 节点数：两子树深度直接相加 left_depth + right_depth 即为边数。
# =============================================