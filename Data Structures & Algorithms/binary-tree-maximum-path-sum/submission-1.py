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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        核心考点：
        - 后序遍历 (DFS 自底向上)。
        - 区分“以当前节点为顶点的拐弯路径”与“向父节点提供的单侧延伸路径”。
        - 负贡献值剪枝 (与 0 取 max)。
        
        时间复杂度：O(N) - 遍历所有节点各一次
        空间复杂度：O(H) - 递归调用栈空间，H 为树的高度
        """
        # 初始化全局最大路径和为负无穷（处理所有节点均为负数的极端情况）
        self.max_sum = float('-inf')

        def max_gain(node: Optional[TreeNode]) -> int:
            """
            辅助函数：计算以 node 为起点的【单侧单链】最大贡献值
            """
            if not node:
                return 0

            # 步骤 1：递归计算左右子树向当前节点贡献的最大单侧路径和
            # 关键剪枝：如果子树贡献为负数，直接舍弃（贡献记为 0）
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 步骤 2：计算以当前 node 为【最高拐弯转折点】的完整路径和
            # 形式为：左分支 + 当前节点 + 右分支（倒 V 形拱桥）
            current_path_sum = node.val + left_gain + right_gain

            # 步骤 3：更新全局最大路径和
            self.max_sum = max(self.max_sum, current_path_sum)

            # 步骤 4：向上层父节点返回【只能选一侧继续向上延伸】的最大路径和
            # $$\text{汇报给父节点的最大贡献} = node.val + \max(left\_gain, right\_gain)$$父节点的视角：只能挑一条“腿”
            return node.val + max(left_gain, right_gain)

        # 触发递归
        max_gain(root)
        return self.max_sum

# ================= 复习速记卡 =================
# 1. 核心公式对比：
#    - 拐弯最大和（更新全局）：node.val + left_gain + right_gain
#    - 单链向上返（函数 return）：node.val + max(left_gain, right_gain)
# 2. 负数剪枝必须记：left_gain = max(dfs(node.left), 0)
# 3. 初始化陷阱：self.max_sum 必须是 float('-inf')，不能设为 0。
# =============================================