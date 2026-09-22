class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        核心考点：
        - 可变长度滑动窗口（求最大长度）。
        - 哈希集合 (Set) 用于 O(1) 判断窗口内是否有重复字符。
        
        时间复杂度：O(2N) = O(N) 
          - 虽然有 while 循环，但每个字符最多被 r 访问进入集合一次，被 l 访问移出集合一次。
        空间复杂度：O(min(N, M)) 
          - N 为字符串长度，M 为字符集大小（如 ASCII 码字符集最多 128 个字符）。
        """
        char_set = set()  # 维护当前滑动窗口 [l, r] 内的所有字符
        l = 0             # 窗口左边界
        res = 0           # 记录全局最长无重复子串的长度

        for r in range(len(s)):
            # 步骤 1：当新加入的字符 s[r] 在窗口内已存在时，窗口处于“非法状态”
            # 不断移动左指针 l，并将移出窗口的字符从 set 中剔除，直到重复字符被移出
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                
            # 步骤 2：将当前字符加入集合（此时窗口 [l, r] 内必定无重复字符）
            char_set.add(s[r])
            
            # 步骤 3：更新无重复子串的最大长度
            res = max(res, r - l + 1)
            
        return res