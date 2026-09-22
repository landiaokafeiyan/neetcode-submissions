from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        核心考点：
        - 可变长度滑动窗口（求最小长度）。
        - 欠账表与 have / need 达标计数机制。
        
        时间复杂度：O(M + N) - M 为 s 的长度，N 为 t 的长度。每个字符最多被 l 和 r 访问各一次。
        空间复杂度：O(K) - K 为字符集大小（ASCII 码最多 128 个键值对）。
        """
        # 边界处理：如果 t 为空或者 s 长度小于 t，不可能找到覆盖子串
        if not t or not s or len(s) < len(t):
            return ""

        # 步骤 1：统计目标字符串 t 中每个字符的需求频次
        count_t = Counter(t)
        window = {}  # 记录当前窗口内各字符的出现频次

        # have: 当前窗口中满足需求数量的字符种类数
        # need: 字符串 t 中总共需要满足的字符种类数
        have, need = 0, len(count_t)
        
        # 记录全局最短窗口的 (长度, 左边界索引, 右边界索引)
        res_len = float("inf")
        res_range = [-1, -1]
        
        l = 0  # 滑动窗口左边界

        # 步骤 2：右指针 r 不断向右探索扩展窗口
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # 如果当前字符是 t 中需要的，且在窗口中的数量刚好达到需求，达标种类数 have + 1
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # 步骤 3：当所有字符种类均已达标 (have == need) 时，尝试收缩左边界 l
            while have == need:
                # 记录/更新当前找到的最优解（更短的子串）
                cur_len = r - l + 1
                if cur_len < res_len:
                    res_len = cur_len
                    res_range = [l, r]

                # 准备将左边界字符移出窗口
                left_char = s[l]
                window[left_char] -= 1
                
                # 如果移出的字符是目标字符，且移出后数量低于了 t 的需求，达标数 have - 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                    
                # 左指针右移，继续尝试寻找更紧凑的窗口
                l += 1

        # 步骤 4：提取结果字符串
        best_l, best_r = res_range
        return s[best_l : best_r + 1] if res_len != float("inf") else ""

# ================= 复习速记卡 =================
# 1. 题型：可变滑动窗口求最小长度（Shortest Window）。
# 2. 状态维护：
#    - need = len(count_t)：表示需要达标的【独立字符种类数】。
#    - have == need 时触发收缩：此时窗口已完全覆盖 t，左指针 l 狂缩直到破坏 have == need。
# 3. 陷阱提醒：
#    - 只有在 window[char] == count_t[char] 的那一刻 have 才能 +1（防止冗余重复字符导致 have 虚高）。
#    - 同理，只有在 window[left_char] < count_t[left_char] 的那一刻 have 才能 -1。
# =============================================