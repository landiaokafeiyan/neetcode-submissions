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

        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

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