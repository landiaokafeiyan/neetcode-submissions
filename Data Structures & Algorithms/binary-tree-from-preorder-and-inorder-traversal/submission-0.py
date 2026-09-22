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

from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        核心考点：
        - 前序 (根左右) 确定根节点，中序 (左根右) 划分左右子树规模。
        - 哈希表 O(1) 定位中序根节点索引。
        - 递归区间指针传递（避免数组 slice 带来的额外时空开销）。
        
        时间复杂度：O(N) - 遍历所有节点各一次，哈希表查找 O(1)。
        空间复杂度：O(N) - 哈希表占用 O(N)，递归栈消耗 O(H)。
        """
        # 步骤 1：建立中序遍历的值到索引的快速映射表
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        # 维护一个全局前序遍历读取指针
        self.pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            """
            根据中序遍历的闭区间 [in_left, in_right] 构建当前子树
            """
            # Base Case：如果中序区间不合法，说明当前子树为空
            if in_left > in_right:
                return None
                
            # 步骤 2：从前序遍历当前位置取出根节点值并创建节点
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1  # 前序指针向后移动一位
            
            # 步骤 3：在中序遍历中找到该根节点的分割点
            mid = inorder_idx[root_val]
            
            # 步骤 4：递归构建左子树与右子树
            # 关键：必须先递归构建左子树，再构建右子树（与 preorder 的访问顺序保持一致）
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root

        return helper(0, len(inorder) - 1)

# ================= 复习速记卡 =================
# 1. 核心映射：
#    - preorder[pre_idx] -> 确定当前子树 Root。
#    - inorder_idx[root_val] -> mid 切分子树。
# 2. 中序区间划定：
#    - 左子树：[in_left, mid - 1]
#    - 右子树：[mid + 1, in_right]
# 3. 递归顺序必须是：先 root.left 再 root.right，因为 self.pre_idx 随着 preorder 单向递增。
# =============================================