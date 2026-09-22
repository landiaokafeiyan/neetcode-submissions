# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    """
    核心考点：
    - 先序遍历 (Preorder DFS: 根 -> 左 -> 右) 序列化。
    - 空节点显式占位符机制 (Null Pointer Placeholder)。
    - 队列 (Queue) 辅助反序列化递归建树。
    
    时间复杂度：
    - serialize: O(N) - 遍历所有节点
    - deserialize: O(N) - 解析每个 token 构建节点
    空间复杂度：
    - O(N) - 序列化字符串与递归栈消耗
    """

    def serialize(self, root: 'TreeNode') -> str:
        """
        将二叉树编码为逗号分隔的字符串
        """
        res = []

        def dfs(node):
            # 遇到空节点，写入占位符 "N"
            if not node:
                res.append("N")
                return
            
            # 先序遍历：先记录当前根节点值，再递归左子树、右子树
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        # 用逗号将所有 token 串联成一个完整的字符串，例如 "1,2,N,N,3,4,N,N,5,N,N"
        return ",".join(res)

    def deserialize(self, data: str) -> 'TreeNode':
        """
        将编码字符串解码还原为二叉树
        """
        # 将字符串按逗号切分，并装入双端队列以便 O(1) 从左向右逐个消耗
        vals = deque(data.split(","))

        def dfs():
            # 步骤 1：弹出当前先序遍历的首个 token
            val = vals.popleft()

            # 步骤 2：如果是空节点占位符，返回 None
            if val == "N":
                return None

            # 步骤 3：创建当前节点
            node = TreeNode(int(val))

            # 步骤 4：严格按照先序遍历的顺序，先递归还原左子树，再还原右子树
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# ================= 复习速记卡 =================
# 1. 序列化公式：dfs(node) -> 记当前值 -> dfs(node.left) -> dfs(node.right)
# 2. 占位符是灵魂：None 节点必须显式输出 "N"，否则无法唯一确定树形。
# 3. 反序列化技巧：将 split 切分后的列表转成 deque，用 popleft() 配合 DFS 自动还原。
# =============================================