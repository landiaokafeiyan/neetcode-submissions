class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        核心考点：
        - 固定长度滑动窗口 (Window Size = len(s1))。
        - 词频统计：使用长度为 26 的数组比较两个子串是否互为排列。
        
        时间复杂度：O(26 * N) = O(N) - N 为 s2 长度，每次滑动比对 26 个小写字母频次
        空间复杂度：O(1) - 仅维护固定大小为 26 的频次数组
        """
        n1, n2 = len(s1), len(s2)
        
        # 边界处理：如果 s1 比 s2 还要长，s2 不可能包含 s1 的排列
        if n1 > n2:
            return False
            
        # 步骤 1：初始化 s1 和 s2 前 n1 个字符的频次统计表
        s1_count = [0] * 26
        window_count = [0] * 26
        
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # 步骤 2：检查初始窗口是否直接匹配
        if s1_count == window_count:
            return True
            
        # 步骤 3：固定窗口向右滑动 (右进左出)
        for i in range(n1, n2):
            # 右侧新字符进入窗口
            window_count[ord(s2[i]) - ord('a')] += 1
            # 左侧旧字符移出窗口
            window_count[ord(s2[i - n1]) - ord('a')] -= 1
            
            # 比较当前窗口频次与 s1 频次是否一致
            if s1_count == window_count:
                return True
                
        return False



################3



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        核心考点：
        - 维护匹配字符种类数 matches (范围 0 到 26)。
        - 滑动过程中动态增减 matches，省去每次比较 26 个数组元素的开销。
        
        时间复杂度：O(N) - 严格单次扫描，单步操作为纯 O(1)
        空间复杂度：O(1)
        """
        if len(s1) > len(s2):
            return False
# 解释： 边界防御/剪枝。如果目标串比母串还要长，任何子串都不可能包含它，直接返回 False 避免后续越界。
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
# 解释：遍历前 n1 个字符，建立初始状态。统计 s1 的全部字符频次。同时，统计 $s_2$ 中第一个窗口（下标 0 到 n1 - 1）的字符频次。
        # matches 统计当前 26 个字母中，频次完全一致的字母个数
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        # 固定窗口开始滑动
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # --- 处理右边界字符进入窗口 ---
            r_idx = ord(s2[r]) - ord('a')
            s2_count[r_idx] += 1
            if s2_count[r_idx] == s1_count[r_idx]:
                matches += 1
            elif s2_count[r_idx] == s1_count[r_idx] + 1:
                matches -= 1

            # --- 处理左边界字符移出窗口 ---
            l_idx = ord(s2[l]) - ord('a')
            s2_count[l_idx] -= 1
            if s2_count[l_idx] == s1_count[l_idx]:
                matches += 1
            elif s2_count[l_idx] == s1_count[l_idx] - 1:
                matches -= 1

            l += 1

        return matches == 26

# ================= 复习速记卡 =================
# 1. 题型归类：定长滑动窗口（Fixed-size Window）。
# 2. 窗口长度：恒定为 len(s1)，指针同步推进（r 从 len(s1) 到 len(s2)）。
# 3. 移入/移出操作：
#    - 进入：window_count[s2[r]] += 1
#    - 移出：window_count[s2[l]] -= 1 (其中 l = r - len(s1))
# =============================================