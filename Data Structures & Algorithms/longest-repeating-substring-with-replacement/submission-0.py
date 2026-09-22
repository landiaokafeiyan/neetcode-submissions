# class Solution:
    # def characterReplacement(self, s: str, k: int) -> int:
        # 这道题的标准最优解法是：滑动窗口（双指针） + 哈希表/数组记录最高频次。
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        核心考点：
        - 可变滑动窗口（求最大长度）。
        - 窗口合法性条件：(窗口长度 - 窗口内最高频字符数) <= k。
        
        时间复杂度：O(N) - 左右指针各遍历字符串一次。
        空间复杂度：O(1) - 字符集仅包含 26 个大写英文字母，哈希表最多存储 26 个键值对。
        """
        count = defaultdict(int)  # 记录当前窗口内每个字符的出现频次
        left = 0                  # 窗口左边界
        max_count = 0             # 记录窗口内出现过的任意单字符的最大频次
        max_len = 0               # 全局最长合法子串长度

        for right in range(len(s)):
            # 步骤 1：右指针字符进入窗口，更新该字符频次
            count[s[right]] += 1
            
            # 步骤 2：更新当前窗口内的最大字符频次
            max_count = max(max_count, count[s[right]])
            
            # 步骤 3：判断当前窗口是否非法
            # 需要替换的字符数 = 当前窗口长度 (right - left + 1) - max_count
            # 如果需要替换的字符数 > k，说明 k 次替换不够用，需要收缩左边界
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1  # 移出左边界字符
                left += 1           # 左指针右移收缩窗口
                
            # 步骤 4：当前窗口已合法，更新最大长度
            max_len = max(max_len, right - left + 1)
            
        return max_len

# ================= 复习速记卡 =================
# 1. 核心判定式：(right - left + 1) - max_count <= k
# 2. 为什么不用堆：Substring 要求连续，且堆无法 O(1) 动态修改指定字符的频次。
# 3. 优化小技巧：max_count 不需要随着 left 的移动而缩小，因为它只负责托底更长的窗口。
# =============================================